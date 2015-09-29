import os
import pyodbc
from glob import glob

server = 'casv-0037'
db = 'PAT_WORKSPACE'
con = pyodbc.connect("Driver={SQL SERVER};SERVER=" + server + ";DATABASE="+ db +";Trusted_Connection=yes")
##con = pyodbc.connect("Driver={SQL SERVER};SERVER = %s;DATABASE = %s" % (server, db))
cursor = con.cursor()

##sqlquery = "select * from sys.tables"
##
##cursor.execute(sqlquery)
##data = cursor.fetchall()
##
##columns = [column [0] for column in cursor.description]
##
##data.insert(0,columns)
##
##for row in data:
##    print row

filelist = glob(r"C:\Users\sarmour\Box Sync\PAT\2015 - EUFL HD\05 - C# Result Information\*.csv")

for f in filelist:
    tblname = os.path.basename(f).rstrip(".csv")
    strsql = "if exists(select name from sys.tables where name = '%s') drop table %s" % (tblname, tblname)
    cursor.execute(strsql)

    strsql = "create table %s (Locid bigint, AAL float)" %tblname
    cursor.execute(strsql)

    strsql = "BULK INSERT %s FROM '%s' WITH (FIELDTERMINATOR = ',', FIRSTROW = 2, ROWTERMINATOR = '\\n')" % (tblname, f)
    print strsql
    cursor.execute(strsql)

