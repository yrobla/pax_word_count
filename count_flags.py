#!/usr/bin/python

from collections import Counter
from csv import DictReader
import re

flags_women = {}
flags_no = {}
keys_binary = ["StDef", "GeMe", "GeLgbti", "GeFa", "JusCr", "JusEm", "JusJu", "JusPri", "JusTra", "NEC", "NatRes", "IntFu", "Ban", "LaRef", "LaNom", "LaCH", "LaEn", "Wat", "SsrGua", "SsrPsf", "SsrFf", "Civso", "Tral",
        "HrGen", "HrCp", "HrSec", "HrMob", "HrDet", "Terr"]
keys_four = ["GCh", "GDis", "GAge", "GMig", "GRa", "GRe", "GInd", "GOth", "GRef", "GSoc", "Pol", "ConRen", "Cons", "Ele", "ElecComm", "PolPar", "Pubad", "Polps", "Terps", "Eps", "Mps", 
    "EqGen", "HrDem", "Prot", "HrFra", "HrNi", "HrIi", "Med", "HrCit", "Dev", "HrDem", "Bus", "Tax", "Ce", "SsrPol", "SsrArm", "SsrDdr", "SsrInt", "Cor", "SsrCrOcr", "SsrDrugs",
    "TjGen", "TjAm", "TjCou", "TjMech", "TjVet", "TjVic", "TjMis", "TjRep", "TjNR"]

with open('pax_all_agreements_data.csv', 'r') as read_obj:
    csv_reader=DictReader(read_obj)
    
    for row in csv_reader:
        # first we sum the agreement with women
        if row["GeWom"] == "1":
            for key in keys_binary:
                if key not in flags_women:
                    flags_women[key] = 0
                if row[key] == "1":
                    # we count if the value is 1
                    flags_women[key]+=1

            for key in keys_four:
                if key not in flags_women:
                    flags_women[key] = 0
                if row[key] == "2" or row[key]=="3":
                    # we count if the value is 2 or 3
                    flags_women[key]+=1
        else:
            # now we go with other
            for key in keys_binary:
                if key not in flags_no:
                    flags_no[key] = 0
                if row[key] == "1":
                    # we count if the value is 1
                    flags_no[key]+=1

            for key in keys_four:
                if key not in flags_no:
                    flags_no[key] = 0
                if row[key] == "2" or row[key]=="3":
                    # we count if the value is 2 or 3
                    flags_no[key]+=1

# first write headers
headers = ["GeWom", ] + keys_binary + keys_four

# write to file
with open("flags.txt", "w+t") as f:
    f.write('{}\n'.format(",".join(headers)))

    # no women
    f.write("0")
    for key in keys_binary + keys_four:
        f.write(",{}".format(flags_no[key]))
    f.write("\n")

    # women
    f.write("1")
    for key in keys_binary + keys_four:
        f.write(",{}".format(flags_women[key]))
    f.write("\n")
