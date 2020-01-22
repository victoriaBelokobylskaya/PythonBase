def int_func(text):
    return str(text).title()


long_str = input('Введите строку, разделенную пробелами: ').split(' ')

new_str = ''

for i in long_str:
    word = int_func(i)
    new_str += str(word) + ' '
print(new_str)

