def fun(input_list):
    return sorted(input_list)
a = [
    [],                    
    [1],                   
    [7, 7, 7, 7],          
    [-5, -1, -3, -2, -4]   
]
for i in a:
    result = fun(i)
    print(result)
