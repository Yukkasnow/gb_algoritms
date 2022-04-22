mass1=[7,2,4,3,8,5,6 ]
max_m=mass1[0]
min_m=mass1[0]
for m in mass1:
    if m>max_m:
        max_m=m
    elif m<min_m:
        min_m=m
mass1[mass1.index(max_m)]=min_m
mass1[mass1.index(min_m)]=max_m
print(mass1)