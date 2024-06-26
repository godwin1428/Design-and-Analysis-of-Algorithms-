a=["abc","car","ada","racecar","cool"]
for i in range(len(a)):
    b=a[i]
    c=b[::-1]
    if b==c:
        break
print(a[i])
