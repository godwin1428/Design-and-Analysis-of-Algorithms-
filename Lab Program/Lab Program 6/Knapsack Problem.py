#KNAPSACK PROBLEM
dat=[[1,2,3,4,5],[3,4,2,5,3],[12,40,10,5,6],[0,0,0,0,0]]
siz=12
for i in range(5):
    dat[3][i]=dat[2][i]/dat[1][i]
sumw=0
sump=0
for i in range(5):
    max=0
    for j in range(5):
        if max<dat[3][j]:
            max=dat[3][j]
            c=j
    dat[3][c]=0
    if sumw<siz:
        sumw+=dat[1][c]
        sump+=dat[2][c]
print("profit:",sump)
