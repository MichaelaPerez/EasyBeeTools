# =============================================================
# TITLE: csv-update-sql.py
# PURPOSE: Convert a csv document into an SQL UPDATE statement
# REQUIREMENTS: python 3.14
# USAGE:
#   Change 'TABLENAME' in to SQL table name
#   Correctly format input and place in same directory
#       (Assumes first column is the sole primary key)
#   Run 'python3.14 csv-update-sql.py' in terminal
#   Admire output (i.e. run in an SQL/MySQL terminal)
# INPUT NAME: 'csv-update-sql-input.py'
# INPUT SAMPLE:
#   mid,mgid,mName
#   236,1,'STERNALIS'
#   238,1,'PECTORALIS MAJOR'
#   255,2,'SUBCLAVIUS'
# OUTPUT NAME: 'csv-update-sql-output.py'
# OUTPUT SAMPLE:
#   UPDATE MUSCLE SET mgid=1,mName='STERNALIS' WHERE mid=236;
# 	UPDATE MUSCLE SET mgid=1,mName='PECTORALIS MAJOR' WHERE mid=238;
# 	UPDATE MUSCLE SET mgid=2,mName='SUBCLAVIUS' WHERE mid=255;
# =============================================================

TABLENAME = 'MUSCLE'

import csv
with open('csv-update-sql-input.csv', encoding="utf8") as csvfile:
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
    outputdml = ""

    # === GET DATA === #
    for r in range(numrow):
        if not r == 0 :
            outputdml = outputdml + "UPDATE " + TABLENAME + " SET "
            for k in range(numcol):
                if not k == 0 :
                    outputdml = outputdml + colnames[k] + "=" + csvdata[r][k]
                    if (numcol-k-1) > 0:
                        outputdml = outputdml + ","
            outputdml = outputdml + " WHERE " + colnames[0] + "=" + csvdata[r][0] + ";\n"

    # print(outputdml)

    tfile = open("csv-update-sql-output.sql", "w")
    tfile.write(outputdml)
    tfile.close()