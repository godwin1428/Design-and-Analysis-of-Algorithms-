def add(a,b):
    c=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            c[i][j]=a[i][j]+b[i][j]
    return c

def mul(a,b):
    c=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
             c[i][j]+=a[i][k]*b[k][j]
    return c

def sub(a,b):
    c=[[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            c[i][j]=a[i][j]-b[i][j]
    return c

a=[[1,2,3,4],    
   [5,6,7,8],   
   [1,2,3,4],     
   [5,6,7,8]]   
b=[[1,2,1,3],
   [1,4,1,5],
   [1,6,1,7],
   [1,8,1,9]]

a11=[[a[0][0],a[0][1]],
     [a[1][0],a[1][1]]]
a12=[[a[0][2],a[0][3]],
     [a[1][2],a[1][3]]]
a21=[[a[2][0],a[2][1]],
     [a[3][0],a[3][1]]]
a22=[[a[2][2],a[2][3]],
     [a[3][2],a[3][3]]]

b11=[[b[0][0],b[0][1]],
     [b[1][0],b[1][1]]]
b12=[[b[0][2],b[0][3]],
     [b[1][2],b[1][3]]]
b21=[[b[2][0],b[2][1]],
     [b[3][0],b[3][1]]]
b22=[[b[2][2],b[2][3]],
     [b[3][2],b[3][3]]]

m1=mul(add(a11,a22),add(b11,b22))
m2=mul(add(a21,a22),b11)
m3=mul(a11,sub(b12,b22))
m4=mul(a22,sub(b21,b11))
m5=mul(add(a11,a12),b22)
m6=mul(sub(a21,a11),add(b11,b12))
m7=mul(sub(a12,a22),add(b21,b22))

c1=add(sub(add(m1,m4),m5),m7)
c2=add(m3,m5)
c3=add(m2,m4)
c4=add(add(sub(m1,m2),m3),m6)

print(c1[0],c2[0])
print(c1[1],c2[1])
print(c3[0],c4[0])
print(c3[1],c4[1])
