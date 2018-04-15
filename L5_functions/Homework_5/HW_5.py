from L5_functions.Homework_5.functoins import card_has_errors, print_bank, mm_yy_has_errors, cvv_has_errors
while True:
    card = input("Your credit number:\n")
    if not card_has_errors(card):
        break
print (card)
print_bank(card)
while True:
    mm_yy = input('Enter the date in this format MM/YY: \n')
    if not mm_yy_has_errors(mm_yy):
        break
while True:
    cvv = input('CVV: \n')
    if not cvv_has_errors(cvv):
        break