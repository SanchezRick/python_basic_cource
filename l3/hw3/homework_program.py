# Номер кредитки
credit_numb = input('Enter your credit card number: \n')
try:
    int(credit_numb)
except ValueError:
    print('Only number!')
    exit()
pass

credit_len = int(len(credit_numb))
if credit_len == 16: # Проверка на наличие 16 символов
    print('Good!')
else:
    print('Must be 16 digits!')
    exit()

# Срок действия
mm, yy = input('Enter the date in this format MM/YY: \n').split('/')
mm = int(mm)
yy = int(yy)
if mm <= 12 and yy <= 99: # Проверка, месяц не больше 12, год не больше 99
    print('OK!')
else:
    print('Eror! Enter the correct data!')
    exit()

# CVV код
cvv = input('CVV: \n')
cvv_len = int(len(cvv))
if cvv_len == 3: # Проверка- код 3-х значный
    print('Good!')
else:
    print('Eror! Must be 3 digits!')
    exit()


print('HA-ha-ha. Now I will use your credit card!\nCredit number: {}\nMM/YY: {}/{}\nCVV: {}'.format (credit_numb, mm, yy, cvv ))