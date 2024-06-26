def bsearch(a,low,high,key):
 mid=int((low+high)/2)
 while(low<=high):
  mid=int((low+high)/2)
  if a[mid]>key:
     high=mid-1
  elif a[mid]<key:
     low=mid+1
  else:
     return mid+1

a=[1,2,3,4,5,6,7,8]
low=0
high=len(a)-1
key=2
print(bsearch(a,low,high,key))
