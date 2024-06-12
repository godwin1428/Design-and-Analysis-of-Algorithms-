a=[5,3,7,2,9,1]
for i in range(len(a)-1):
    for j in range(0,len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
print(a)
