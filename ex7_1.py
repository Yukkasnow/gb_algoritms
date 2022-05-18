import random
def bubble_sort(spisok):
    swapped = False
    for i in range(len(spisok)  -1, 0,-1):
        for j in range(i):
            if spisok[j] < spisok[j + 1]:
                spisok[j], spisok[j + 1] = spisok[j + 1], spisok[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return spisok


if __name__ == '__main__':
    s = []
    for i in range(-100,101):
        s.append(random.randrange(-100,101))
    print(s)
    print(bubble_sort(s))


