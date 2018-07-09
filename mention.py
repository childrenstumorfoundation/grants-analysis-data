# search through all text files of the pdf, and search from the string tumor foundation.

import glob
import codecs
import regex as re

nomentionList = []
def searchByMention(list):

    # Define regular expression-based searches

    ctf = re.compile("(Children's Tumor Foundation){e<=4}",flags=re.IGNORECASE)
    ctf1 = re.compile("ctf", re.I)
    nnf = re.compile("(National Neurofibromatosis Foundation){e<=1}", flags=re.IGNORECASE)

    for i in range(0, len(list)):
        filename = list[i]
        print(str(filename))
        textname = str(filename).replace('.pdf', '.txt')
        file = codecs.open(str(textname), encoding = 'utf-8')
        # load it once
        filetext = file.read()

        if re.search(ctf, filetext) or re.search(ctf1, filetext) or re.search(nnf, filetext):
            print("YES")
        else:
            print('NO')
            nomentionList.append(filename)

mylist = glob.glob("C:\\Users\\cliu\\PycharmProjects\\1\\*.pdf")
final_list = []
for i in range (0, len(mylist)):
    mystring = mylist[i]
    nameList = mystring.split('\\')
    filename = nameList[len(nameList) - 1]
    final_list.append(filename)
searchByMention(final_list)
print("Following are a list of files without 'CTF' mention")
print(nomentionList)
print(len(nomentionList))
