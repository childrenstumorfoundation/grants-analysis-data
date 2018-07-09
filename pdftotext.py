
# if want HTML instead of plaintext, switch TextConverter to HTMLConverter
import glob
import os
import re

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

nomentionList = []
def convert_pdf_to_txt(path):

    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    mypath = (path.split('.pdf'))[0]
    file = open((str(mypath) + '.txt'), 'wb')

    # don't write anything if the file isn't empty
    if os.stat(str(mypath) + '.txt').st_size == 0:
        file.write(text.encode("utf-8"))
    file.close()
    fp.close()
    device.close()
    retstr.close()

mylist = glob.glob("C:\\Users\\cliu\\PycharmProjects\\1\\*.pdf")

for i in range (0, len(mylist)):
    mystring = mylist[i]
    nameList = mystring.split('\\')
    filename = nameList[len(nameList) - 1]
    print()
    print(filename)

    convert_pdf_to_txt(filename)