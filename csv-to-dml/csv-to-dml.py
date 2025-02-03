# =============================================================
# TITLE: csv-to-dml.py
# PURPOSE: Convert a csv document into an SQL insert statement
# REQUIREMENTS: python 3.14
# USAGE:
#   Change 'TABLENAME' in to SQL table name
#   Correctly format input and place in same directory
#   Run 'python3.14 csv-to-dml.py' in terminal
#   Admire output (i.e. run in an SQL/MySQL terminal)
# INPUT NAME: 'csv-to-dml-input.py'
# INPUT SAMPLE:
#   mid,mgid,mName
#   236,1,'STERNALIS'
#   238,1,'PECTORALIS MAJOR'
#   255,2,'SUBCLAVIUS'
#   267,4,'SUBCLAVIUS ANTERIOR'
#   252,5,'EXTERNAL INTERCOSTAL'
# OUTPUT NAME: 'csv-to-dml-output.py'
# OUTPUT SAMPLE:
#   INSERT INTO MUSCLE (mid,mgid,mName) VALUES 
# 	    (236,1,'STERNALIS'),
# 	    (238,1,'PECTORALIS MAJOR'),
# 	    (255,2,'SUBCLAVIUS'),
# 	    (267,4,'SUBCLAVIUS ANTERIOR'),
# 	    (252,5,'EXTERNAL INTERCOSTAL');
# =============================================================

TABLENAME = 'MUSCLE_GROUP'

import csv
with open('csv-to-dml-input.csv', encoding="utf8") as csvfile:
    spamreader = list(csv.reader(csvfile))

    # === COPY DATA INTO 2X2 LIST === #
    csvdata = []
    i=0
    for row in spamreader:
        if i==0 :
            colnames = list(row)
        else :
            csvdata.append(list(row))
        i = i+1
    numcol = len(colnames)
    numrow = len(csvdata)

    # === GET COLUMN NAMES === #
    outputdml = "INSERT INTO " + TABLENAME + " ("
    for j in range(numcol):
        outputdml += colnames[j]
        if j < numcol-1 :
            outputdml += ","
        else :
            outputdml += ") VALUES \n\t(" # last col in row

    # === GET DATA === #
    for r in range(numrow):
        for k in range(numcol):
            outputdml += csvdata[r][k]
            if k < numcol-1 :
                outputdml += ","
            elif r < numrow-1:
                outputdml += "),\n\t("
            else :
                outputdml += ");"
    # print(outputdml)

    tfile = open("csv-to-dml-output.sql", "w")
    tfile.write(outputdml)
    tfile.close()