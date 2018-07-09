# enter a multiline string of IDOs in the command line argument, the program finds all the grant numbers contained in the pdf, and
# adds the IDO to cells with corresponding grant numbers

import regex as re
import glob
import codecs

# 1, PDF:
# finds all pathnames that match a specific pattern
list_with_grantnum = []

def searchByGrantNum(mylist):
# grantRegex = re.compile(r'\d{4}-\d{2}-\d{3}')
    grantRegex = re.compile("(\d{4}-\d{2}-\d{3}){e<=1}")
#ctf = re.compile("(Children's Tumor Foundation){e<=4}", flags=re.IGNORECASE)
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
