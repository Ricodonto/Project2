import random
import string
from datetime import datetime, timedelta

def generate_date():
    # Generate a random date between 7th April and 18th April
    start_date = datetime(2024, 4, 7)
    end_date = datetime(2024, 4, 18)
    random_date = start_date + timedelta(days=random.randint(0, (end_date - start_date).days))
    return random_date.strftime('%d/%m/%Y')

def generate_route():
    # Generate a random route: two random locations separated by a hyphen
    locations = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']
    start = random.choice(locations)
    end = random.choice(locations)
    while start == end:  # Ensure start and end are different
        end = random.choice(locations)
    return f"{start}-{end}"

def generate_status():
    # Generate a random status: 'AVAILABLE' or 'BROKEN DOWN'
    return random.choice(['AVAILABLE', 'BROKEN DOWN'])

def generate_data():
    data = []
    for i in range(1, 21):
        route = generate_route()
        status = generate_status()
        date = generate_date()
        email = f"{route.lower().replace(' ', '-')}@sample.com"
        data.append((i, route, status, date, email))
    return data

# Generate data
data = generate_data()

# Print the generated data
for item in data:
    print(item)