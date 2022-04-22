mass=[1,2,8,8,6,7,7,9,3,3,4,8,5,1,8,6,8]
print(mass)
total=0
for m in mass:
    count=mass.count(m)
    if count>total:
        total=count
        max_number=m
print(f'{max_number} встречается {total} раз')