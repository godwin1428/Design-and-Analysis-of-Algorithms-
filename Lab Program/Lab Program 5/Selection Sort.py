a=[5,3,7,2,9,1]
for i in range(len(a)-1):
    mini=i
    for j in range(i,len(a)):
        if a[mini]>a[j]:
            mini=j
        a[i],a[mini]=a[mini],a[i]
print(a)
