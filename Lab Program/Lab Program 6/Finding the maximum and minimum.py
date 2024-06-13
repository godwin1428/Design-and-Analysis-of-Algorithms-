a=[9,7,2,-8,1,3,6,5]
min=a[0]
max=a[0]
for i in range(len(a)):
    if min>a[i]:
        min=a[i]
    if max<a[i]:
        max=a[i]
print("maximum:",max)
print("minimum:",min)
