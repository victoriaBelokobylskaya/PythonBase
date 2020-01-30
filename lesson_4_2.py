from random import randint

generator = [randint(1,100) for el in range(30)]
print(generator)
new_list = []
for k, el in enumerate(generator):
    if generator[k] > generator[k-1]:
        new_list.append(el)


print(new_list)