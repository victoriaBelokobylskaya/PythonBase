from itertools import cycle


# if __name__ == '__main__': - почему, когда добавляю эту проверку, у меня выходит ошибка импорта?
def new_cycle(l, c):
    cy_list = []
    i = 0
    for item in cycle(l):
        if i > c:
            break
        else:
            cy_list.append(item)
            i += 1
    return cy_list
