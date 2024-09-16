import csv
from faker import Faker
import random

def generate_csv(filename, num_rows):
    fake = Faker()
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for _ in range(num_rows):
            first_name = fake.first_name()
            last_name = fake.last_name()
            address = fake.address().replace('\n', ', ')
            date_of_birth = fake.date_of_birth(minimum_age=18, maximum_age=90).isoformat()
            writer.writerow({
                'first_name': first_name,
                'last_name': last_name,
                'address': address,
                'date_of_birth': date_of_birth
            })

if __name__ == '__main__':
    num_rows = 1000000  # Adjust this number as needed
    generate_csv('sample_data.csv', num_rows)
