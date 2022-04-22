mass=[1,2,2,9,8,7,1,3]
max=None
min=None
summ=0
for m in mass:
    if max==None and min==None:
        max=m
        min=m
    elif m>max:
        max=m
    elif m<min:
        min=m

if mass.index(min)<mass.index(max):
    for m in mass[mass.index(min)+1:mass.index(max)]:
        summ+=m
elif mass.index(max)<mass.index(min):
    for m in mass[mass.index(max)+1:mass.index(min)]:
        summ+=m
print(summ)
