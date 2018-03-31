def print_my_name(name):
    if len(name) < 4:
        print('You good!')
    print(f"You name is {name}")


print_my_name('De')


def my_sum(a, b, c=1):
    return c * (a + b)


x = my_sum(5, 6)
y = my_sum(5, 6, 2)
print(x)
print(y)


import random
for i in range(5):
    print(random.randint(4, 9))

