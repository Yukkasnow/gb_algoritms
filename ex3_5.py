mass=[1,5,-10,-20,-5,3,4,-20]
max_num=None
minus=0
for m in mass:
    if m<0:
        minus=m
        if max_num==None:
            max_num=minus
        if minus>max_num:
            max_num=minus

print(max_num)