import pyodbc

connection = pyodbc.connect("Driver = {SQL Server Native Client 11.0};"
                            "Server = UKO-FAMILY\SQLEXPRESS;"
                            "Database = Mydatabase;"
                            "Trusted_Connection = yes;")

cursor = connection.cursor()
cursor.execute('Select Top(20) * FROM CovidDeath$')

for row in cursor:
    print(f'row = {row}')