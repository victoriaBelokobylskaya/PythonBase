from itertools import count


def new_count(s, e):
    c_list = []
    for el in count(s):
        if el > e:
            break
        else:
            c_list.append(el)
    return c_list
