"""
@author: Jakob Balkovec
@date: Mon 12th Feb 2024

@brief:  This script generates hashes for 10 words sourced from the English dictionary. 
         These hashes are intended as mock data for [Milestone3]. 
         Note: The hashing technique may change due to limited PHP library availability.
"""

from bcrypt import hashpw, gensalt
from faker import Faker

PASSWORD_FILEPATH: str = r"/Users/jbalkovec/Desktop/CPSC/CPSC 3300/Q_Project/Data/mock_passwords.txt"
EMAIL_FILEPATH: str = r"/Users/jbalkovec/Desktop/CPSC/CPSC 3300/Q_Project/Data/mock_emails.txt"
PHONE_FILEPATH: str = r"/Users/jbalkovec/Desktop/CPSC/CPSC 3300/Q_Project/Data/mock_phone.txt"

def write_to_file(data: list, filepath: str) -> None:
    with open(filepath, "w") as file:
        for item in data:
            if isinstance(item, bytes):
                # if item is in bytes format, decode it to string before writing
                file.write(item.decode() + "\n")
            else:
                file.write(item + "\n")
    return None

# define words to hash as byte strings
words_to_hash = [
    b'Accommodation', b'Accomplishment', b'Archaeological', b'Entrepreneurial',
    b'Extracurricular', b'Incomprehensible', b'Antidepressant', b'Counterargument',
    b'Disappointment', b'Irresponsible'
]

# hash each word and store in a list (list-comprehension)
passwords = [hashpw(word, gensalt()) for word in words_to_hash]
write_to_file(passwords, PASSWORD_FILEPATH)

# call constructor
fake = Faker()

# create 10 mock emails
emails = [fake.email() for _ in range(10)]
write_to_file(emails, EMAIL_FILEPATH)

# create 10 mock phone numbers
phone_numbers = [fake.phone_number() for _ in range (10)]
write_to_file(phone_numbers, PHONE_FILEPATH)