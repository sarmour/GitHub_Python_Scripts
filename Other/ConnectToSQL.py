import pyodbc

##cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=master')
##cursor = cnxn.cursor()

##cursor.execute("select name from sys.databases")
##dblist = []
##for row in cursor:
##    print row.name
##    dblist += row.name

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=PAT_NAHU_Master')
cursor = cnxn.cursor()

sqlquery = 'select * from sys.tables'

cursor.execute(sqlquery)
data = cursor.fetchall()

columns = [column [0] for column in cursor.description]

print columns

for row in data:
    print row
