def per(arr, n):
    if n == 0:
        return [[]]
    if len(arr) < n:
        return []  
    res = []
    for i in range(len(arr)):
        fis = arr[i]
        rem = arr[:i] + arr[i+1:]
        for perm in per(rem, n - 1):
            res.append([fis] + perm)
    return res
a = [1, 2, 3]
n = 3
print(per(a, n))
