def comb(arr, k):
    if k == 0:
        return [[]]
    if len(arr) < k:
        return []
    
    result = []
    for i in range(len(arr)):
        f = arr[i]
        rem = arr[i+1:]
        for c in comb(rem, k-1):
            result.append([f] + c)
    return result

m = input("Enter elements of the list separated by spaces: ").split()
k = int(input("Enter the length of combinations: "))

combinations = comb(m, k)
formatted_combinations = [','.join(comb) for comb in combinations]
print('[' + ', '.join(['[' + combo + ']' for combo in formatted_combinations])+']')
