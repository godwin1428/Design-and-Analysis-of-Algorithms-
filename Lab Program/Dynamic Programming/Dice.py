def printcombo(c,n):
    for i in range(n):
        print(c[i],end="")
    print("")
def generate(d,n,curr,tar):
    if curr==n:
        sum=0
        for i in range(n):
            sum+=d[i]
        if sum==tar:
            printcombo(d,n)
        return
    for i in range(1,6+1):
        d[curr]=i
        generate(d,n,curr+1,tar)
n=3 #no of dice
tar=10 #target MANO MASS
dice={}
generate(dice,n,0,tar)
