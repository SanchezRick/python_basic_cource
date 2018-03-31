#Card number
card_number = 1
while card_number == 1:
    card_number = input('Your credit card:\n')
    card_list = card_number.split(' ')
    for i in card_list:
        if len(i) == 4 and len(card_list) == 4:
            try:
                card_int = int(i)
            except:
                card_number = 1
                print('Incorrect!')
                break
        else:
            card_number = 1
            print('Incorrect number!')
            break
print('Nice!')
privat = 5167
monobank = 5375
if card_list[0] == privat:
    print('You use PrivatBank credit card')
elif card_list[0] == monobank:
    print('You use Monobank credit card')
else:
    print('You use credit card from the unknown bank')

# MM/YY
mm = 0
while mm == 0:
    mm, yy = input('Enter the date in this format MM/YY: \n').split('/')
    try:
        mm = int(mm)
        yy = int(yy)
    except:
        mm = 0
        print('Incorrect date!')
        continue

    if mm <= 12 and yy <= 99 and mm > 0 and yy >= 18: # Проверка, месяц не больше 12, год не больше 99
        print('OK!')
        break
    else:
        mm = 0
        print('Error! Enter the correct data!')
        continue

# CVV код
cvv = 1
while cvv == 1:
    cvv = input('CVV: \n')
    try:
        cvv_int = int(cvv)
    except:
        cvv = 1
        print('Incorrect cvv!')
        continue
    cvv_len = int(len(cvv))
    if cvv_len == 3: # Проверка- код 3-х значный
        print('Good!')
        print('HA-ha-ha. Now I will use your credit card!\nCredit number: {}\nMM/YY: {}/{}\nCVV: {}'.format(card_number, mm, yy, cvv))
    else:
        cvv = 1
        print('Error! Must be 3 digits!')
        continue
