# Prim's Algorithm
def prims(G):
    INF = 9999999
    V = 5
    selected = [0, 0, 0, 0, 0]
    no_edge = 0
    selected[0] = True
    print("Edge : Weight")
    while (no_edge < V - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if ((not selected[j]) and G[i][j]):  
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        print(str(x) + " - " + str(y) + " : " + str(G[x][y]))
        selected[y] = True
        no_edge += 1

#kruskals algorithm
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])

def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def kruskals(G):
    V = len(G)
    edges = []
    
    for i in range(V):
        for j in range(i+1, V):
            if G[i][j] != 0:
                edges.append((G[i][j], i, j))
    
    edges.sort()
    parent = []
    rank = []
    
    for node in range(V):
        parent.append(node)
        rank.append(0)
    
    MST = []
    edge_count = 0
    index = 0
    
    while edge_count < V - 1:
        w, u, v = edges[index]
        index = index + 1
        x = find(parent, u)
        y = find(parent, v)
        
        if x != y:
            edge_count = edge_count + 1
            MST.append((u, v, w))
            union(parent, rank, x, y)
        
    print("Edge : Weight")
    for u, v, weight in MST:
        print(str(u) + "-" + str(v) + " : " + str(weight))

#boruvkas algorithm
def findi(parent, i):
    if parent[i] == i:
        return i
    return findi(parent, parent[i])

def unioni(parent, rank, x, y):
    xroot = findi(parent, x)
    yroot = findi(parent, y)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

def boruvkas(G):
    V = len(G)
    parent = []
    rank = []
    cheapest = []

    for node in range(V):
        parent.append(node)
        rank.append(0)
        cheapest.append([-1, float('inf')])
    
    numTrees = V

    print("Edge : Weight")

    while numTrees > 1:
        for i in range(V):
            for j in range(V):
                if G[i][j] != 0:
                    u = findi(parent, i)
                    v = findi(parent, j)
                    if u != v:
                        if G[i][j] < cheapest[u][1]:
                            cheapest[u] = [j, G[i][j]]
                        if G[i][j] < cheapest[v][1]:
                            cheapest[v] = [i, G[i][j]]

        for i in range(V):
            if cheapest[i][0] != -1:
                u = i
                v = cheapest[i][0]
                w = cheapest[i][1]
                set_u = findi(parent, u)
                set_v = findi(parent, v)
                
                if set_u != set_v:
                    print(str(u) + " - " + str(v) + " : " + str(w))
                    unioni(parent, rank, set_u, set_v)
                    numTrees -= 1

        cheapest = [[-1, float('inf')] for _ in range(V)]

G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

print("Prims Algorithm:")
prims(G)
print("\nkruskals Algorithm:")
kruskals(G) 
print("\nBoruvkas Algorithm:")
boruvkas(G)
