n=5
k=3
coef=1
sum=0
for i in range(n):
    for j in range(i+1):
        if j==0 or i==0:
            coef=1
        else:
            coef=coef*(i-j+1)/j
        if j==k-1:
            sum+=coef
print(int(sum))
