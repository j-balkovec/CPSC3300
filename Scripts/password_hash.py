"""
@author: Jakob Balkovec
@date: Mon 12th Feb 2024

@brief:  This script generates hashes for 10 words sourced from the English dictionary. 
         These hashes are intended as mock data for [Milestone3]. 
         Note: The hashing technique may change due to limited PHP library availability.
"""

from bcrypt import hashpw, gensalt

FILEPATH: str = r"/Users/jbalkovec/Desktop/CPSC/CPSC 3300/Q_Project/Data/mock_passwords.txt"
# define words to hash as byte strings
words_to_hash = [
    b'Accommodation', b'Accomplishment', b'Archaeological', b'Entrepreneurial',
    b'Extracurricular', b'Incomprehensible', b'Antidepressant', b'Counterargument',
    b'Disappointment', b'Irresponsible'
]

# hash each word and store in a list (list-comprehension)
passwords = [hashpw(word, gensalt()) for word in words_to_hash]

# write them to a file
with open(FILEPATH, "w") as file:
    for password in passwords:
        file.write(password.decode('utf-8') + '\n')

    
