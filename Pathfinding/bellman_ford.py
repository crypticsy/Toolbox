import os


class bellmanford:
    nodes, distance, edges = {},{},set()

    def __init__(self, cost, edges):
        self.nodes,self.edges = cost, edges
        for i in edges:
            self.distance[i] = float('inf')

    def start(self,n):
        self.distance[n] = 0

        for i in range(len(self.edges)):
            change = False

            for j in self.nodes.keys():
                cost = self.distance[j[0]] + self.nodes[j] 
                if cost < self.distance[j[1]]:
                    self.distance[j[1]] = cost
                    change = True

            if i != len(self.edges)-1 and not change:
                print(i)
                for i in self.distance.keys():
                    print("Value for",i,"is",self.distance[i])
                break
            elif i == len(self.edges)-1:
                print("Negative cycle seen")
        


# Testing

path = os.path.dirname(os.path.abspath(__file__))
values = open( path +'\\bellman.txt','r')

cost,edges = {},set()
for i in values:
    temp = list(map(int, i.split()))
    cost[(temp[0],temp[1])] = temp[2]
    edges.add(temp[0]);edges.add(temp[1])


test = bellmanford( cost,edges)
test.start(1)       #final all shortest path from the this point