import random
def merge_sort(spisok):
    if len(spisok) < 2:
        return spisok
    pivot = spisok.pop()
    left_lst, equal_lst, right_lst = [], [pivot], []
    for i in spisok:
        if i == pivot:
            equal_lst.append(i)
        elif i < pivot:
            right_lst.append(i)
        else:
            left_lst.append(i)
    return merge_sort(left_lst) + equal_lst + merge_sort(right_lst)
s=[]
for i in range(0,51):
    s.append(random.randrange(0,51))
print(s)
print(merge_sort(s))