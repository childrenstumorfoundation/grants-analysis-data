# it writes the local storage and filename column to publication

import openpyxl
wb = openpyxl.load_workbook('Publication.xlsx')
sheet = wb['selection']
numRow = sheet.max_row

for i in range (2,numRow+1):
    doi = sheet['E'+str(i)].value
    filename = str(doi).replace('/','_') + '.pdf'
    sheet['J'+str(i)] = filename

    filename = sheet['J' + str(i)].value
    pdfloc = "grants-analysis-data\\papers\\pdf\\" + str(filename)
    sheet['I' + str(i)] = pdfloc

    textname = str(filename).replace('.pdf', '.txt')
    textloc = "grants-analysis-data\\papers\\txt\\" + str(textname)
    sheet['K' + str(i)] = textloc

    sheet['L' + str(i)] = textname

wb.save('Publication.xlsx')
