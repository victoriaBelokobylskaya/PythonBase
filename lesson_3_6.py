# def int_func(text):
#     return str(text).title()

long_str = input('Введите строку, разделенную пробелами: ').split(' ')

new_str = ''
word = lambda text: str(text).title()

for i in long_str:
    # word = int_func(i)
    new_str += str(word(i)) + ' ' # переделала на lambda функцию
print(new_str)

