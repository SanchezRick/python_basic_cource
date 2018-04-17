import re
pattern = re.compile(r'(^\+[0-9]{12}$)',)
name = (input('Your name surename:'))
rev_name = name[::-1]
rev_name_title = rev_name.title()
print(rev_name_title)
number = input('Number?')
print(pattern.match(number))
with open("practice.txt", "r+") as my_practice
    my_practice.write()
