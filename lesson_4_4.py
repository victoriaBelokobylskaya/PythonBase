from random import randint

new_list = [randint(1, 300) for i in range(30)]
print(new_list)

print([el for el in new_list if new_list.count(el) == 1])