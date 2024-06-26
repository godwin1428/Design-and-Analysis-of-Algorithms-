def climb(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    ons = 2
    two = 1
    for i in range(3, n + 1):
        current = ons + two
        two = ons
        ons = current
    return ons
print(climb(4))  
print(climb(3))
