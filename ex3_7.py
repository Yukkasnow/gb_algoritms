mass=[1,2,8,6,1,3,2] #1,2
min_1=mass[0]
min_2=mass[1]

for m in mass:
    if m<min_1:
        min_1=m
    elif m<min_2:
        min_2=m
    else:
        continue
print(min_1,min_2)