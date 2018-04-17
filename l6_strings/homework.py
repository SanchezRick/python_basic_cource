from l6_strings.strings_hw.functions import name_has_errors, card_has_errors, print_bank, mm_yy_has_errors, cvv_has_errors

while True:
    name_surname = input("Your last, second name:\n")
    if name_has_errors(name_surname) == True:
        break
while True:
    card_number = input("Your credit number:\n")
    if card_has_errors(card_number) == True:
        break
print_bank(card_number)
while True:
    mm_yy = input('Enter the date in this format MM/YY: \n')
    if mm_yy_has_errors(mm_yy) == True:
        break
while True:
    cvv = input('CVV: \n')
    if cvv_has_errors(cvv) == True:
        break
print("Name:\n{}\nCard number\n{}\nMM/YY\n{}\nCVV\n{}".format(name_surname.title(), card_number, mm_yy, cvv))