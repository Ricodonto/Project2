import pypyodbc as odbc
import random
# 'ODBC Driver 17 for SQL Server'
# 'SQL SERVER'
DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = r'LAPTOP-KICEGSLT'
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


def random_index():
    l = random.sample(range(1,21), 20)
    return l


def generate_name():
    # Generate random first and last names
    first_names = ['John', 'Emma', 'Michael', 'Sophia', 'Matthew', 'Olivia', 'William', 'Ava', 'James', 'Isabella']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    return random.choice(first_names), random.choice(last_names)

def generate_data():
    data = []
    vehicle = random_index()
    official = random_index()
    for i in range(1, 21):
        first_name, last_name = generate_name()
        email = f"{first_name.lower()}.{last_name.lower()}@sample.com"
        data.append((i, first_name, last_name, email, vehicle[i-1], official[i-1]))
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

for item in data:
    print(item)

SQL_STATEMENT = """
INSERT INTO drivers(driver_id, fname, lname, email, vehicle_id, official_id)
VALUES 
"""

for item in generate_str(data):
    SQL_STATEMENT = SQL_STATEMENT + item

# # SQL_STATEMENT = """
# # select * from officials;
# # """

# # select * from officials;
cursor.execute(SQL_STATEMENT)

cursor.commit()