#Import the module
from faker import Faker
import pandas as pd

# Initialize the Faker object and set up a seed 

fake = Faker()
Faker.seed(13)

# Dictionary with 100 entries of data
## !!! Note that "Email" and "First/Last Name" currently do not correlate with email

def generate_dummy_data(num_entries=100):
    data={
        'First Name':[],
        'Last Name':[],
        'Email':[],
        'Phone Number':[],
        'Location':[],
        'Profession':[],
        'Company':[],
        'Date':[],
        'Price':[],
        'Hardware':[],
        'Amount':[]
    }

    for _ in range(num_entries):
        data['First Name'].append(fake.first_name())
        data['Last Name'].append(fake.last_name())
        data['Email'].append(f"{fake.first_name()}.{fake.last_name()}@{fake.free_email_domain()}")
        data['Phone Number'].append(fake.phone_number())
        data['Location'].append(fake.country())
        data['Profession'].append(fake.job())
        data['Company'].append(fake.company())
        data['Date'].append(fake.date_between(start_date='-1y', end_date='+1y'))
        data['Price'].append(fake.pyint())
        data['Hardware'].append(fake.numerify(text='Laptop Intel Core i%'))
        data['Amount'].append(fake.random_digit())

    return data
    
#Generate the data
dummy_data = generate_dummy_data(100)

#Create a DataFrame
df_dummy_data = pd.DataFrame(dummy_data)

#Save to a CSV file
df_dummy_data.to_csv('dummy_data.csv', index=False)

print(df_dummy_data.head())
