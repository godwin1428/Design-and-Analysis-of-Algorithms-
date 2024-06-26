nums1 = [4,3,2,3,1]
nums2 = [2,2,5,2,3,6]
c1=0
c2=0
for i in nums1:
    if i in nums2:
        c1+=1
for i in nums2:
    if i in nums1:
        c2+=1
print("[",c1,",",c2,"]")
