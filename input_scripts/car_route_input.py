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


def generate_license_plate():
    # Generate a random license plate format
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    numbers = ''.join(random.choices(string.digits, k=3))
    last_letter = random.choice(string.ascii_uppercase)
    return f"K{letters}{numbers}{last_letter}"

def generate_route():
    # Generate a random route: two random locations separated by a hyphen
    locations = ['Kajiado', 'Kisumu', 'Kiambu', 'Machakos', 'Nyeri']
    start = random.choice(locations)

    return f"Nairobi-{location}"

def generate_status():
    # Generate a random status: 'AVAILABLE' or 'BROKEN DOWN'
    return random.choice(['AVAILABLE', 'BROKEN DOWN'])

def generate_capacity():
    # Generate a random capacity: 4, 6, or 14
    return random.choice([4, 6, 14])

def generate_data():
    data = []
    location = ['Kajiado', 'Kisumu', 'Kiambu', 'Machakos', 'Nyeri']
    for i in range(1,6):
        start = 'Nairobi'
        route = f"{start}-{location[i-1]}"
        data.append((i, route))
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
INSERT INTO car_route(route_id, car_route)
VALUES 
"""

for item in generate_str(data):
    SQL_STATEMENT = SQL_STATEMENT + item

# SQL_STATEMENT = """
# select * from vehicle;
# """

print(SQL_STATEMENT)

# select * from officials;
cursor.execute(SQL_STATEMENT)

conn.commit()
# rows = cursor.fetchall()

# for row in rows:
#     print(row)