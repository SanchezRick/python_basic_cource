
name = input ('What is our name?: ')
age = input('How old are you?: ')
email = '{}{}@itea.ua'.format(name, age)
print(email)
try:
    name / 'sometext'
    name = 'Noob'
    print(name)
except TypeError:
    surname = 'Trololo'
    print(surname)
print('\nDeveloping with Python...\n')
print('Ti dopustil oshibku!' if surname == 'Noob' else 'Molodec!')

"""

name = int(input ('What is our name?: '))
age = input('How old are you?: ')
email = '{}{}@itea.ua'.format(name, age)
print(email)
try:
    name / 1
    surname = 'Noob'
    print(surname)
except TypeError:
    surname = 'Trololo'
    print(surname)
print('\nDeveloping with Python...\n')
print('Ti dopustil oshibku!' if surname == 'Noob' else 'Molodec!')
"""

