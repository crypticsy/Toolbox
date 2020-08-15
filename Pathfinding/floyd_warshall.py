import os

#   Testng
path = os.path.dirname(os.path.abspath(__file__))
values = open( path +'\\floyd_warshall.txt','r')

cost,edges = {},set()
for i in values:
    temp = list(map(int, i.split()))
    cost[(temp[0],temp[1])] = temp[2]       # adding weight for each node
    edges.add(temp[0]);edges.add(temp[1])   # finding all possible edges

edges = list(edges)


def floydWarshall():        #useful for cases with negative weights
    for i in edges:
        for j in edges:
            if i == j:cost[(i,j)] = 0
            elif (i,j) not in cost:cost[(i,j)] = float('inf')

    for a in edges:
        for i in edges:
            for j in edges:
                if i!=j and i!=a and j!=a:      # cases where the co-ord isn't diagonal, vertical or horizontal in the matrix
                    cost[(i,j)] = min(cost[(i,j)], cost[(i,a)] + cost[(a,j)] )

    for a in edges:
        if cost[(a,a)] < 0 : print("Graph contains negative cycle")




floydWarshall()

for i in edges:
    for j in edges:
        print((i,j),"costs:",cost[(i,j)])