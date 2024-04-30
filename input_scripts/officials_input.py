import pypyodbc as odbc
import random
import string
# 'ODBC Driver 17 for SQL Server'
# 'SQL SERVER'
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = r'DESKTOP-5IS51HK'
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


def generate_phone_number():
    # Generate a random phone number starting with '07' or '01'
    start = random.choice(['07', '01'])
    rest = ''.join(random.choices(string.digits, k=8))
    return start + rest

def generate_name():
    # Generate random first and last names
    first_names = ['John', 'Emma', 'Michael', 'Sophia', 'Matthew', 'Olivia', 'William', 'Ava', 'James', 'Isabella']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    return random.choice(first_names), random.choice(last_names)

def generate_data():
    data = []
    for i in range(1, 21):
        first_name, last_name = generate_name()
        phone_number = generate_phone_number()
        email = f"{first_name.lower()}.{last_name.lower()}@sample.com"
        data.append((i, first_name, last_name, phone_number, email))
    return data

# Generate data
data = generate_data()

def generate_str(data):
    values = []
    for i in range(len(data)):
        if i < len(data)-1:
            value = f"{data[i]},"
        else:
            value = f"{data[i]};"
        values.append(value)
    return values

SQL_STATEMENT = """
INSERT INTO official(official_id, fname, lname, phone_number, email)
VALUES 
"""

for item in generate_str(data):
    SQL_STATEMENT = SQL_STATEMENT + item

# SQL_STATEMENT = """
# select * from officials;
# """

# select * from officials;
cursor.execute(SQL_STATEMENT)

# rows = cursor.fetchall()

# for row in rows:
#     print(row)