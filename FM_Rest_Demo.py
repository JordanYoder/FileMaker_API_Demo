import fmrest
from tabulate import tabulate
fmrest.__version__

fms = fmrest.Server(
    '',
    user='',
    password='',
    database='',
    layout='',
    verify_ssl=False,
    # if you are testing without cert/domain you may need the parameter verify_ssl=False here.
)

fms.login()

# Get all records
all_customers = fms.get_records()
for customer in all_customers:
    print(f'{customer.FirstName} {customer.LastName}\n'
          f'{customer.Company}\n'
          f'{customer.Address} {customer.City}, {customer.State} {customer.Zip}\n'
          f'{customer.Web} \n'
          f'{customer.Email}\n'
          f'{customer.Phone1}\n'
          f'{customer.Phone2}\n')

state = input("Perform find for State (abbreviation): ")

# Perform a find
find_query = [{'State': state}]
foundset = fms.find(find_query)
for record in foundset:
    print(f'{record.FirstName} {record.LastName}\n'
          f'{record.Company}\n'
          f'{record.Address} {record.City}, {record.State} {record.Zip}\n'
          f'{record.Web} \n'
          f'{record.Email}\n'
          f'{record.Phone1}\n'
          f'{record.Phone2}\n')

# Create new record
first = input('Enter first name: ')
last = input('Enter last name: ')
address = input('Enter Street Address: ')
city = input('Enter City: ')
state = input('Enter State:')
zip = input('Enter Zip: ')

newrecord = fms.create_record({'FirstName': first,
                               'LastName': last,
                               'Address': address,
                               'City': city,
                               'State': state,
                               'Zip': zip,
                               })

