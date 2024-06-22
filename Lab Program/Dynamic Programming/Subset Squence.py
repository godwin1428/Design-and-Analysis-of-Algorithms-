def subsets(s):  
    if len(s) == 0:  
        return [[]]  
    x = subsets(s[:-1])  
    return x + [[s[-1]] + y for y in x]  
s = [1, 2, 3]  
result = subsets(s)  
print(result)
