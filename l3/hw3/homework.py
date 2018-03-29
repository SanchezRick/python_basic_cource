# input
mm, yy = input('Enter the date MM/YY: \n').split('/')
a, b, c = map(int, input().split())

# try, except
numb = input('Number: ')
try:
    print(numb + 100000)
except ValueError:
    print('Is not number!')
    numb = 'N/A'
mm, yy = input('Enter the date in this format MM/YY: \n').split('/')
number = 99999
try:
    kkk = 1 / 0
except ZeroDivisionError:
    kkk = 0
# IF
if number <= 12:
    print('OK!')
else:
    print('Eror!)
mm = 10
yy = 9
if mm <= 12 and yy <= 99: # Проверка, месяц не больше 12, год не больше 99
    print('OK!')
else:
    print('Eror! Enter the correct data!')
    exit()