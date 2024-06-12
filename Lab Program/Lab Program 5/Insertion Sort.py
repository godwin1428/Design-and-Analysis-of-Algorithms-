a=[5,3,7,2,9,1]
for i in range(1,len(a)):
    j=i
    while(j>0 and a[j]<a[j-1]):
        a[j],a[j-1]=a[j-1],a[j]
        j=j-1
print(a)
