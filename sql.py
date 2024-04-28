import pypyodbc as odbc
# 'ODBC Driver 17 for SQL Server'
# 'SQL SERVER'
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = r'LAPTOP-KICEGSLT\SQLEXPRESS01'
DATABASE_NAME = 'carpooling'

# uid=<username>;
# pwd=<password>;

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    Trust_Connection=yes;
    uid=Rico;
    pwd=test;
"""

conn = odbc.connect(connection_string, autocommit=True)
print(conn)

cursor = conn.cursor()

SQL_STATEMENT = """
insert into test(ID, CarName) 
values('2', 'Prius');
"""
cursor.execute("select * from test;")
rows = cursor.fetchall()

for row in rows:
    uid, carname, city, salary = row
    print(uid)
