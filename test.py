import random
import string


def generate_license_plate():
    # Generate a random license plate format
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    numbers = ''.join(random.choices(string.digits, k=3))
    last_letter = random.choice(string.ascii_uppercase)
    return f"K{letters}{numbers}{last_letter}"

def generate_status():
    # Generate a random status: 'AVAILABLE' or 'BROKEN DOWN'
    return random.choice(['AVAILABLE', 'BROKEN DOWN'])

def generate_capacity():
    # Generate a random capacity: 4, 6, or 14
    return random.choice([4, 6, 14])

def generate_data():
    data = []
    for i in range(1, 21):
        license_plate = generate_license_plate()
        status = generate_status()
        capacity = generate_capacity()
        data.append((i, license_plate, status, capacity))
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

# Print the generated data
for item in data:
    print(type(item))

for _ in range(1,21):
    print(_)