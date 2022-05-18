import random


def gnome_sort(lst):
    i = 1
    while i < len(lst):
        if lst[i - 1] <= lst[i]:
            i += 1
        else:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
            if i == 0:
                i = 1
    return lst
m=50
s=[]
for i in range(0,2*m+1):
    s.append(random.randint(0,2*m+1))
print(s)
print(gnome_sort(s),'\n', gnome_sort(s)[len(s)//2])