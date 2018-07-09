# enter a multiline string of IDOs in the command line argument, the program finds all the grant numbers contained in the pdf, and
# adds the IDO to cells with corresponding grant numbers

import regex as re
import glob
import codecs
import openpyxl

# 1, PDF:
# finds all pathnames that match a specific pattern
list_with_grantnum = []
dictionary = {}

def searchByGrantNum(mylist):
# grantRegex = re.compile(r'\d{4}-\d{2}-\d{3}')
    grantRegex = re.compile("(\d{4}-\d{2}-\d{3}){e<=1}")

    for i in range(0, len(mylist)):
        filename = mylist[i]
        print(str(filename))
        textname = str(filename).replace('.pdf', '.txt')
        file = codecs.open(str(textname), encoding = 'utf-8')
        # load it once
        filetext = file.read()

        list = re.findall(grantRegex,filetext)
        if len(list) == 0:
            # doesn't find the grant number in the publication:
            print('NO')

        else:
            list_remove = []
            for strings in list:
                d = 0
                for c in strings:
                    if c.isdigit():
                        d=d+1
                if d!=9 or strings.count('-')!=2 or len(strings)<11:
                    # make sure the string has the 9 digits and two hyphens
                    list_remove.append(strings)
            list=[x for x in list if x not in list_remove]
            if len(list)==0:
                print('no')
            else:
                print(str(len(list)) + ' grant numbers')
                print(str(list)+'\n')
                list_with_grantnum.append(filename)
                dictionary[filename]=list

mylist = glob.glob("C:\\Users\\cliu\\PycharmProjects\\1\\*.pdf")
final_list = []
for i in range (0, len(mylist)):
    mystring = mylist[i]
    nameList = mystring.split('\\')
    filename = nameList[len(nameList) - 1]
    final_list.append(filename)

searchByGrantNum(final_list)
print('Following is the list of files with grant number:')
print(list_with_grantnum)
print(len(list_with_grantnum))

print('file, grant pairs:')
print(dictionary)

# enter paperID and grantID into a seperate excel named workbook1

wb = openpyxl.load_workbook('Workbook1.xlsx')
sheet = wb['Sheet1']

for i in range(0, len(list_with_grantnum)):
    sheet['A'+str(i+2)]= list_with_grantnum[i] 
    string = str(list_with_grantnum[i]).replace('_', '/')
    doi_string = string.split('.pdf')[0]
    sheet['C'+str(i+2)] =doi_string
    sheet['B'+str(i+2)]=str(dictionary[list_with_grantnum[i]])
    
wb.save('Workbook1.xlsx')
