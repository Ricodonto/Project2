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

try:
    conn = odbc.connect(connection_string, autocommit=True)
    print(conn)
except odbc.DatabaseError:
    print("login information incorrect")
    exit()

conn = odbc.connect(connection_string, autocommit=True)
cursor = conn.cursor()

SQL_STATEMENT = """
ALTER TABLE officials
ALTER COLUMN official_id int;
"""

# select * from officials;
cursor.execute(SQL_STATEMENT)
rows = cursor.fetchall()

for row in rows:
    print(row)