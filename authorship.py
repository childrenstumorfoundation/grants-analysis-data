
# the program takes the "researcher" cell in the ctf-grant excel, search for it in publication pdfs,
# and find all files that the author appears in
import openpyxl
import codecs
import regex as re
from openpyxl.utils import get_column_letter as c_l

wb = openpyxl.load_workbook('CTF-Grant.xlsx')
sheet = wb.active
numRow = sheet.max_row

wb1 = openpyxl.load_workbook('Publication.xlsx')
sheet1 = wb1['selection']
numRow1 = sheet1.max_row

wb2 = openpyxl.load_workbook('Workbook2.xlsx')
sheet2 = wb2.active
numRow2 = sheet2.max_row

name_not_appear = []
def searchByAuthorshipDate(list):
    dictionary = {}
    mylist=[]

    for rowindex in range (3,numRow+1):
        author = sheet['O'+str(rowindex)].value
        mylist.append(author)
        endYear = sheet['N'+str(rowindex)].value
        dictionary.setdefault(author, []).append(endYear)

    finallist = set(mylist)
    a = 2
# loop through all author names:
    for name in finallist:
        authorname = re.compile(str(name), re.I)
        print(str(name)+':  '+ str(dictionary[name]))
        sheet2['A' + str(a)]=name
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

#  date approach
        dictionary2 = {}
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

list1= ['10.1001_jama.2009.1663.pdf', '10.1001_jamaophthalmol.2013.7649.pdf', '10.1002_ajmg.a.33045.pdf', '10.1002_ajmg.a.33183.pdf', '10.1002_ajmg.a.33189.pdf', '10.1002_ajmg.a.34359.pdf', '10.1002_ajmg.a.35535.pdf', '10.1002_ajmg.a.35760.pdf', '10.1002_ajmg.a.36312.pdf', '10.1002_ajmg.a.36754.pdf', '10.1002_ajmg.a.36793.pdf', '10.1002_ajmg.a.37089.pdf', '10.1002_ajmg.a.37723.pdf', '10.1002_ajmg.a.38239.pdf', '10.1002_ajmg.b.31063.pdf', '10.1002_ana.24659.pdf', '10.1002_da.22468.pdf', '10.1002_humu.22026.pdf', '10.1002_humu.22832.pdf', '10.1002_ijc.27976.pdf', '10.1002_jbmr.1992.pdf', '10.1002_jbmr.2316.pdf', '10.1002_jbmr.2538.pdf', '10.1002_jbmr.528.pdf', '10.1002_jor.22628.pdf', '10.1002_mus.23324.pdf', '10.1002_path.1909.pdf', '10.1002_path.4427.pdf', '10.1002_pbc.23015.pdf', '10.1002_pbc.25546.pdf', '10.1002_stem.1990.pdf', '10.1007_978-3-642-75747-1.pdf', '10.1007_s00401-011-0905-0.pdf', '10.1007_s00401-016-1583-8.pdf', '10.1007_s10897-007-9101-8.pdf', '10.1007_s10897-014-9688-5.pdf', '10.1007_s11060-007-9501-5.pdf', '10.1007_s11060-016-2150-9.pdf', '10.1007_s11060-017-2581-y.pdf', '10.1007_s11832-010-0293-3.pdf', '10.1007_s12035-017-0653-9.pdf', '10.1007_s13311-017-0518-y.pdf', '10.1007_s40474-015-0060-8.pdf', '10.1016_j.ajhg.2007.09.011.pdf', '10.1016_j.ajhg.2008.01.011.pdf', '10.1016_j.ajhg.2017.12.001.pdf', '10.1016_j.ajo.2014.06.017.pdf', '10.1016_j.ajpath.2014.04.006.pdf', '10.1016_j.ajpath.2015.10.023.pdf', '10.1016_j.anucene.2017.05.041.pdf', '10.1016_j.biochi.2017.01.001.pdf', '10.1016_j.bone.2011.09.043.pdf', '10.1016_j.bone.2013.11.013.pdf', '10.1016_j.cancergen.2014.04.001.pdf', '10.1016_j.cancergen.2015.02.003.pdf', '10.1016_j.cancergencyto.2005.04.003.pdf', '10.1016_j.ccell.2014.09.009.pdf', '10.1016_j.ccell.2015.09.007.pdf', '10.1016_j.ccell.2018.01.005.pdf', '10.1016_j.ccr.2005.07.004.pdf', '10.1016_j.ccr.2008.01.003.pdf', '10.1016_j.ccr.2008.12.006.pdf', '10.1016_j.ccr.2009.05.009.pdf', '10.1016_j.ccr.2011.02.017.pdf', '10.1016_j.ccr.2011.08.014.pdf', '10.1016_j.ccr.2011.12.027.pdf', '10.1016_j.ccr.2012.02.010.pdf', '10.1016_j.ccr.2014.02.017.pdf', '10.1016_j.ccr.2014.05.001.pdf', '10.1016_j.cell.2007.07.020.pdf', '10.1016_j.cell.2008.09.060.pdf', '10.1016_j.cell.2010.01.029.pdf', '10.1016_j.celrep.2013.08.011.pdf', '10.1016_j.celrep.2013.12.001.pdf', '10.1016_j.celrep.2014.09.036.pdf', '10.1016_j.chembiol.2012.07.005.pdf', '10.1016_j.cmet.2006.10.010.pdf', '10.1016_j.conb.2017.08.003.pdf', '10.1016_j.cub.2005.09.043.pdf', '10.1016_j.cub.2006.02.063.pdf', '10.1016_j.cub.2007.11.066.pdf', '10.1016_j.devcel.2017.02.004.pdf', '10.1016_j.expneurol.2017.09.008.pdf', '10.1016_j.febslet.2012.03.016.pdf', '10.1016_j.jgg.2011.08.003.pdf', '10.1016_j.jneuroim.2010.05.002.pdf', '10.1016_j.mce.2011.07.039.pdf', '10.1016_j.molcel.2006.05.011.pdf', '10.1016_j.mrfmmm.2007.07.015.pdf', '10.1016_j.neuron.2017.05.020.pdf', '10.1016_j.neuroscience.2005.09.030.pdf', '10.1016_j.neuroscience.2009.03.006.pdf', '10.1016_j.neuroscience.2018.02.025.pdf', '10.1016_j.neuroscience.2018.04.002.pdf', '10.1016_j.nicl.2017.06.032.pdf', '10.1016_j.nucengdes.2017.03.032.pdf', '10.1016_j.nucengdes.2018.03.028.pdf', '10.1016_j.pscychresns.2017.06.003.pdf', '10.1016_j.semcdb.2016.06.002.pdf', '10.1016_j.str.2013.07.008.pdf', '10.1016_j.ymgme.2018.02.009.pdf', '10.1016_S0960-9822(03)00492-5.pdf', '10.1016_S0968-0004(98)01224-9.pdf', '10.1016_S1097-2765(03)00382-4.pdf', '10.1016_S1471-4914(02)00008-4.pdf', '10.1016_S1534-5807(01)00009-0.pdf', '10.1021_acs.jproteome.5b00466.pdf', '10.1021_ml400251g.pdf', '10.1038_35002593.pdf', '10.1038_35005118.pdf', '10.1038_bjc.2016.354.pdf', '10.1038_ejhg.2014.220.pdf', '10.1038_embor.2012.11.pdf', '10.1038_gim.2018.28.pdf', '10.1038_labinvest.2016.88.pdf', '10.1038_nature08902.pdf', '10.1038_nature08987.pdf', '10.1038_nature10406.pdf', '10.1038_nature13561.pdf', '10.1038_nature21376.pdf', '10.1038_nature711.pdf', '10.1038_ncponc115.pdf', '10.1038_ng.2552.pdf', '10.1038_ng.2641.pdf', '10.1038_ng.2855.pdf', '10.1038_ng1059.pdf', '10.1038_nm.3583.pdf', '10.1038_nn.3348.pdf', '10.1038_nn.4159.pdf', '10.1038_nrc3911.pdf', '10.1038_nrc866.pdf', '10.1038_onc.2010.363.pdf', '10.1038_onc.2012.587.pdf', '10.1038_onc.2013.320.pdf', '10.1038_onc.2015.252.pdf', '10.1038_onc.2016.269.pdf', '10.1038_onc.2016.464.pdf', '10.1038_s41467-017-00346-5.pdf', '10.1056_NEJMoa0902579.pdf', '10.1056_NEJMoa1605943.pdf', '10.1073_pnas.0503224102.pdf', '10.1073_pnas.0901932106.pdf', '10.1073_pnas.0913297108.pdf', '10.1073_pnas.1004829107.pdf', '10.1073_pnas.1103418108.pdf', '10.1073_pnas.1306431110.pdf', '10.1073_pnas.1424563112.pdf', '10.1073_pnas.1508545112.pdf', '10.1073_pnas.1512570112.pdf', '10.1073_pnas.1525349113.pdf', '10.1073_pnas.1607298113.pdf', '10.1073_pnas.1610531113.pdf', '10.1073_pnas.191107698.pdf', '10.1074_jbc.M112.378695.pdf', '10.1074_jbc.M113.510933.pdf', '10.1083_jcb.141.7.1589.pdf', '10.1083_jcb.200608009.pdf', '10.1083_jcb.201503081.pdf', '10.1091_mbc.e05-05-0403.pdf', '10.1093_brain_awt327.pdf', '10.1093_emboj_17.15.4313.pdf', '10.1093_hmg_ddt515.pdf', '10.1093_hmg_ddu414.pdf', '10.1093_hmg_ddv019.pdf', '10.1093_jpepsy_jsr124.pdf', '10.1093_neuonc_noq012.pdf', '10.1093_neuonc_nor072.pdf', '10.1093_neuonc_nos076.pdf', '10.1093_neuonc_not150.pdf', '10.1093_neuonc_not242.pdf', '10.1093_neuonc_nou059.pdf', '10.1093_neuonc_now032.pdf', '10.1097_00125817-200205000-00002.pdf', '10.1097_01.mlg.0000240185.14224.7d.pdf', '10.1097_MOO.0b013e328357d2ee.pdf', '10.1101_gad.1054603.pdf', '10.1101_gad.1054703.pdf', '10.1101_gad.12.8.1121.pdf', '10.1101_gad.1466806.pdf', '10.1101_gad.1587907.pdf', '10.1101_gad.190876.112.pdf', '10.1101_gad.1938710.pdf', '10.1101_gad.1957110.pdf', '10.1101_gad.1964810.pdf', '10.1101_gad.862101.pdf', '10.1111_bjd.14873.pdf', '10.1111_cge.12551.pdf', '10.1111_his.13135.pdf', '10.1111_j.1399-0004.2011.01637.x.pdf', '10.1111_jcpp.12344.pdf', '10.1111_nan.12330.pdf', '10.1126_sciadv.aao5520.pdf', '10.1126_science.1068452.pdf', '10.1126_science.286.5447.2172.pdf', '10.1126_science.286.5447.2176.pdf', '10.1126_scisignal.2004060.pdf', '10.1126_scisignal.2004125.pdf', '10.1126_scisignal.aas9473.pdf', '10.1128_MCB.00248-09.pdf', '10.1128_MCB.00332-09.pdf', '10.1128_MCB.00609-10.pdf', '10.1128_MCB.00630-15.pdf', '10.1128_MCB.01450-08.pdf', '10.1136_jmedgenet-2013-101951.pdf', '10.1136_jmg.2008.059907.pdf', '10.1136_jmg.2009.075721.pdf', '10.1136_jmg.37.12.933.pdf', '10.1136_jnnp.2006.108134.pdf', '10.1146_annurev-neuro-060909-153215.pdf', '10.1146_annurev-pathol-011811-132441.pdf', '10.1146_annurev.pathol.2.010506.091940.pdf', '10.1155_2012_620834.pdf', '10.1158_0008-5472.CAN-03-3798.pdf', '10.1158_0008-5472.CAN-05-3330.pdf', '10.1158_0008-5472.CAN-05-3759.pdf', '10.1158_0008-5472.CAN-07-5849.pdf', '10.1158_0008-5472.CAN-09-0143.pdf', '10.1158_0008-5472.CAN-09-3107.pdf', '10.1158_0008-5472.CAN-09-3769.pdf', '10.1158_0008-5472.CAN-10-1219.pdf', '10.1158_0008-5472.CAN-12-1888.pdf', '10.1158_1078-0432.CCR-08-3011.pdf', '10.1158_1078-0432.CCR-12-3167.pdf', '10.1158_1535-7163.MCT-09-0834.pdf', '10.1158_1541-7786.MCR-11-0425-T.pdf', '10.1158_1541-7786.MCR-12-0593.pdf', '10.1158_2159-8290.CD-14-0159.pdf', '10.1172_JCI28271.pdf', '10.1172_JCI28341.pdf', '10.1172_JCI60578.pdf', '10.1172_JCI62727.pdf', '10.1172_JCI71048.pdf', '10.1172_JCI85183.pdf', '10.1182_blood-2006-05-025395.pdf', '10.1182_blood-2012-05-378596.pdf', '10.1182_blood-2013-05-500272.pdf', '10.1186_1471-2474-11-105.pdf', '10.1186_1741-7015-9-82.pdf', '10.1186_1755-8794-2-42.pdf', '10.1186_s12859-015-0485-4.pdf', '10.1186_s12864-017-3519-7.pdf', '10.1186_s13013-015-0041-z.pdf', '10.1186_s40478-014-0082-1.pdf', '10.1212_01.wnl.0000435743.49414.b6.pdf', '10.1212_01.wnl.0000435748.79908.c5.pdf', '10.1212_NXG.0000000000000169.pdf', '10.1212_NXG.0000000000000192.pdf', '10.1212_WNL.0000000000001129.pdf', '10.1212_WNL.0000000000002927.pdf', '10.1212_WNL.0000000000002928.pdf', '10.1212_WNL.0000000000002929.pdf', '10.1212_wnl.0000000000002930.pdf', '10.1212_WNL.0000000000002932.pdf', '10.1212_WNL.0000000000002933.pdf', '10.1212_WNL.0b013e31821e55b0.pdf', '10.1242_dmm.009779.pdf', '10.1242_dmm.025783.pdf', '10.1242_jcs.059469.pdf', '10.1242_jcs.098343.pdf', '10.1371_journal.pgen.1002281.pdf', '10.1371_journal.pgen.1003958.pdf', '10.1371_journal.pgen.1006198.pdf', '10.1371_journal.pgen.1006516.pdf', '10.1371_journal.pone.0035524.pdf', '10.1371_journal.pone.0046900.pdf', '10.1371_journal.pone.0052874.pdf', '10.1371_journal.pone.0078880.pdf', '10.1371_journal.pone.0096114.pdf', '10.1371_journal.pone.0119093.pdf', '10.1371_journal.pone.0159718.pdf', '10.1371_journal.pone.0178316.pdf', '10.1371_journal.pone.0178639.pdf', '10.1373_clinchem.2007.090290.pdf', '10.1373_clinchem.2008.112821.pdf', '10.1542_peds.2009-1684.pdf', '10.1634_theoncologist.2012-0162.pdf', '10.1677_ERC-09-0068.pdf', '10.18632_oncotarget.1422.pdf', '10.18632_oncotarget.1609.pdf', '10.18632_oncotarget.251.pdf', '10.18632_oncotarget.2810.pdf', '10.18632_oncotarget.4858.pdf', '10.18632_oncotarget.793.pdf', '10.3171_2011.6.JNS11131.pdf', '10.3174_ajnr.A4405.pdf', '10.3389_fonc.2016.00259.pdf', '10.3389_fonc.2017.00058.pdf', '10.4161_cc.9.16.12713.pdf', '10.4161_rdis.28341.pdf', '10.4236_ijcm.2015.612128.pdf', '10.7554_eLife.11123.pdf', '10.7554_eLife.14713.pdf', '10.7554_eLife.23966.pdf']
list2 = list1
for r in range (0, len(list1)):
    list2[r]= list1[r].replace('.pdf', '.txt')

searchByAuthorshipDate(list)
wb2.save('Workbook2.xlsx')

print(len(name_not_appear))







