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


def random_index(r):
    l = random.sample(range(1,r+1), 20)
    return l



def generate_name():
    # Generate random first and last names
    first_names = ['John', 'Emma', 'Michael', 'Sophia', 'Matthew', 'Olivia', 'William', 'Ava', 'James', 'Isabella']
    last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor']
    return random.choice(first_names), random.choice(last_names)

SQL_STATEMENT = """
select car_route from car_route;
"""

l_route = cursor.execute(SQL_STATEMENT)

car_route = []

for tup in l_route:
    car_route.append(tup[0])

def generate_data(car_route):
    data = []
    route = random_index(5)
    driver = random_index(20)
    c_route = random.choices(car_route, 20)
    pickuptime = random.sample(['08:00', '09:00', '10:00'], 20)
    for i in range(1, 21):
        first_name, last_name = generate_name()
        email = f"{first_name.lower()}.{last_name.lower()}@sample.com"
        data.append((i, route[i-1], pickuptime[i-1], email, driver[i-1], c_route[i-1]))
    return data

# Generate data
data = generate_data(car_route)

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
INSERT INTO car_group(group_id, route_id, pickuptime, driver_id, car_route)
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