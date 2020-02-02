from functools import reduce

new_list = [i for i in range(99, 1001) if i % 2 == 0]
print(new_list)

print(reduce((lambda a, b: a * b), new_list))
