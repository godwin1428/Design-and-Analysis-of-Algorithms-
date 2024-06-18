nV = 5
INF = 999
def floyd(G):
    dis = list(map(lambda i: list(map(lambda j: j, i)), G))
    for k in range(nV):
        for i in range(nV):
            for j in range(nV):
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j])
    printt(dis)
def printt(dis):
    for i in range(nV):
        for j in range(nV):
            if(dis[i][j] == INF):
                print("INF", end=" ")
            else:
                print(dis[i][j], end="  ")
        print(" ")


G = [[0, 3, INF, INF ,2],
     [INF,0, 2, INF, INF],
     [INF,INF, 0,2, INF],
     [INF,INF,INF,0,2],
     [INF,3, 3,INF,0]]
floyd(G)
