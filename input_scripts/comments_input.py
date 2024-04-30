import pypyodbc as odbc
import random
import string
from datetime import datetime, timedelta
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


def random_index():
    l = random.sample(range(1,21), 20)
    return l

def generate_date():
    # Generate a random date between 7th April and 18th April
    start_date = datetime(2024, 4, 7)
    end_date = datetime(2024, 4, 18)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%d/%m/%Y')

def generate_comment():
    # Generate a random status: 'AVAILABLE' or 'BROKEN DOWN'
    return random.choice(['Scratching', ' Delay', 'Aggresive', 'Driving under the influence'])

def generate_data():
    data = []
    driver = random_index()
    official = random_index()
    for i in range(1, 6):
        date = generate_date()
        comment = generate_comment()
        data.append((i, comment, date, driver[i-1], official[i-1]))
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
INSERT INTO comments(comment_id, comment, date_submitted, driver_id, official_id)
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