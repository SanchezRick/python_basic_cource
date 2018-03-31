def print_my_name(name, surname, age: int):
    if age < 25:
        print('Hello {} {}. You are young enough'.format(name, surname))
    elif age >= 25:
        print('Hello {} {}. You are old'.format(name, surname))


# print_my_name('Denis', 'Nechasniuk', 21)

def print_my_age(age: int, year=2018):
    return year - age

