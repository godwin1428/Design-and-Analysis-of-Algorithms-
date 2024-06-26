nums = [3,1,2,2,2,1,3]
k = 4
count=0
for i in range(len(nums)):
    for j in range(i):
        if nums[i]==nums[j]:
            c=i*j
            if c%2==0:
                count+=1
print(count)
