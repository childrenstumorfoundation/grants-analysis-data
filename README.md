# grants-analysis-data
Data used for papers->grants analysis project

papers.csv: exported from Zotero, contains the metadata of publication files retrieved by Zotero
(Create another tab with relevant columns, eg: publication year, author, title, doi, url, date, file attachment )

grants.csv: exported from Dimension, contains grant information for all publications sponsored by CTF

1. naming.py
- extract a list of filenames under the current working directory
- loop through each filename, find its respective row in "Publication1.xlsx"(the paper csv) by comparing it to the "file attachment" column , and rename the file based on the "DOI" column.

2. pdftotext.py
- after renaming all publication papers with DOIs, convert pdf files into separate text files under the same name (with different suffix), using 'pdfminer' module, (supports unicode)

3. grantNum_ctfmention.py
- function "searchByGrantNum": searches for the string formatted as ctf issued grant number,(eg: '2006-01-A' /'2008-10-001' / '2012A-05-001' /'2013-04-002B') in all files.
- function "searchByMention": searches for "ctf" string in the list of files returned by the first function ( with grant numbers), (eg: 'Children's Tumor Foundation' / 'ctf' / 'National Neurofibromatosis Foundation' / 'nnf')
- enter the confirmed files' paperID & grantID in a separate excel, named Workbook1.xlsx

confirmed_paperID-grantIS.csv : renamed the Workbook1.xlsx, and converted it into csv files

4. authorship.py
- the program takes the "researcher" column in the "ctf-grant excel" (grants.csv), and searches for each of them in all publication files, and for each author, returns the list of files the author appears in.
- for each publication within the list, compare its publication year (according to paper.csv) with all grant end years associated with the author (grants.csv), if the publication comes after the grant end year, add it to the list of potential papers that are related to the author and the specific grant end year.
(column paper1-paper6 corresponds to each grant end year the researcher applied, from left to right )
