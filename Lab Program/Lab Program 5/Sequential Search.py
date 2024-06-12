a=[5,3,7,2,9,1]
key=1
flag=0
for i in range(len(a)):
    if key==a[i]:
        flag=1
        break
if flag==1:
    print("element found at index value",i+1)
else:
    print("element not found")
