# the program searches for researcher strings (according to CTF-Grant excel) in each publication file
# and find all papers the author's name appears in

import openpyxl
import codecs
import regex as re
from openpyxl.utils import get_column_letter as c_l

# given the list of publications where the same author name appears,
# the program find the one with publication date closest to the grant end year,
# and narrow down the possible publication of a grant to one.

wb = openpyxl.load_workbook('CTF-Grant.xlsx')
sheet = wb.active
numRow = sheet.max_row

wb1 = openpyxl.load_workbook('Publication.xlsx')
sheet1 = wb1['selection']
numRow1 = sheet1.max_row

wb2 = openpyxl.load_workbook('author_grantyear_paperIDs.xlsx')
sheet2 = wb2.active
numRow2 = sheet2.max_row

name_not_appear = []

def searchByAuthorshipDate(list):
# build a dictionary to pair up the author - grant start year:
    dictionary = {}
# build a list of author names in text format, without the duplicates.
    mylist=[]

    for rowindex in range (3,numRow+1):
        author = sheet['O'+str(rowindex)].value
        mylist.append(author)
        startYear = sheet['L'+str(rowindex)].value
        # use a nested list within a dictionary to store more than one value(grant end year) to the key(author)
        dictionary.setdefault(author, []).append(startYear)

# the set() built-in function get unique collection of author names.
    finallist = set(mylist)
    a = 2
# loop through all author names:
    for name in finallist:
        authorname = re.compile(str(name), re.I)
        # authorname = re.compile("(str(name)){e<2}", re.I)
        print(str(name)+':  '+ str(dictionary[name]))
        # text file name
        sheet2['A' + str(a)]=name
        # grant year
        sheet2['B'+str(a)]=str(dictionary[name])

        listTOdate = []
        for i in range(0, len(list)):
            file = codecs.open(str(list[i]), encoding='utf-8')
            # load it once
            filetext = file.read()

            if re.search(authorname, filetext):
                listTOdate.append(list[i])
        print("papers with the author's name")
        print(listTOdate)

        if len(listTOdate)==0:
            name_not_appear.append(name)

# 3, date approach
# get the publication year of the list of publication papers from publication.xlsx
        dictionary2 = {}
        # pair up grant year and paper names
        for publication in listTOdate:
            for rowindex1 in range (2,numRow1+1):
                if publication == sheet1['L'+str(rowindex1)].value:
                    publicationyear = sheet1['B' + str(rowindex1)].value
            list_grantyear = dictionary[name]

            column = 3
            for i in range(0, len(list_grantyear)):
                if list_grantyear[i] <= publicationyear:
                    dictionary2.setdefault(list_grantyear[i],[]).append(publication)
                    if sheet2[c_l(column+i) + str(a)].value == None:
                        sheet2[c_l(column+i) + str(a)] = publication
                    else:
                        newvalue = str(sheet2[c_l(column+i) + str(a)].value) + ' , '+ str(publication)
                        sheet2[c_l(column + i) + str(a)]=newvalue
                else:
                    print('grant year:'+str(list_grantyear[i]) + '  publication year:'+str(publicationyear))
                    print(str(publication)+' is not possible')
        a+=1
        print(dictionary2)

list = []
for row in range (2, numRow1):
    filename = sheet1['L'+str(row)].value
    list.append(filename)

searchByAuthorshipDate(list)
wb2.save('author_grantyear_paperIDs.xlsx')

print(name_not_appear)
print(len(name_not_appear))




