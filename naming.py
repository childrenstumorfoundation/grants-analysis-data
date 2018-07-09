# read the list of link attachment, get the current file name
import openpyxl
import os
import glob

wb = openpyxl.load_workbook('Publication1.xlsx')
sheet = wb['selection']
numRow = sheet.max_row
dictionary = {}
notonlist = []
nodoi = []
# create a list of filenames stored within Zotero
mylist = glob.glob("C:\\Users\\cliu\\PycharmProjects\\2\\*.pdf")
final_list = []
for i in range (0, len(mylist)):
    mystring = mylist[i]
    nameList = mystring.split('\\')
    filename = nameList[len(nameList) - 1]
    final_list.append(filename)

# create a dictionary that connects the pdf file name to its doi
# create a list of original pdf file names: link
# create a list of doi future names: doi
for int1 in range(2, numRow):
    list1 = []
    link = sheet['H'+str(int1)].value
    if link == None:
        print('the row with the title '+sheet['D'+str(int1)].value + '  has no pdf attached to it' )
        continue
    list1 = link.split('\\')
    name = list1[len(list1)-1]

    doi = sheet['E'+str(int1)].value
    futurename = str(doi)+'.pdf'
    dictionary[name]=futurename
    # rename function in os module:
for files in final_list:
    #print(files)
    if files not in dictionary:
        #print("the pdf's doi cannot be found in the publication excel")
        notonlist.append(files)
    else:
        string = dictionary[files]
        if string == 'None.pdf':
            print(files)
            #print("the pdf doesn't have a doi associated with it in the publication excel")
            nodoi.append(files)
        else:
            # list of files on the excel, with doi associated, and are renamed
            mystring1 = string.replace('/', '_')
    # Slash in DOI is being replaced with an Underscore
            os.renames(str(files),str(mystring1))

print('\n'+"the pdf's doi cannot be found in the publication excel")
print(notonlist)
print(len(notonlist))

print('\n'+" the pdfs without associated dois, in the publication excel")
print(nodoi)
print(len(nodoi))
print('\n'+'Total amount of files')
print(len(final_list))

