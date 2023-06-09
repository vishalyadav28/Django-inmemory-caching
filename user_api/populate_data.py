import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'user_api.settings')

import django
django.setup()

from faker import Faker
from users.models import User

def populate_data(num_records):
    fake = Faker()
    
    for _ in range(num_records):
        name = fake.name()
        # age = fake.age()
        # salary = fake.salary()
        
        user = User(name=name)
        user.save()

if __name__ == '__main__':
    num_records = 10  # Number of records you want to populate
    populate_data(num_records)