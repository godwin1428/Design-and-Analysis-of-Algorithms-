def fun(s):
    result = []
    n = len(s)
    i = 0
    while i < n:
        start = i
        while i < n - 1 and s[i] == s[i + 1]:
            i += 1
        if i - start + 1 >= 3:
            result.append([start, i])
        i += 1
    return result
print(fun('abbxxxxzzy')) 
print(fun('abc'))
