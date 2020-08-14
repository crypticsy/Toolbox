import os


class bellmanford:
    edges, distance, nodes = {},{},set()

    def __init__(self, cost, nodes):
        self.edges,self.nodes = cost, nodes
        for i in nodes:
            self.distance[i] = float('inf')

    def start(self,n):
        self.distance[n] = 0

        for i in range(len(self.nodes)):
            change = False

            for j in self.edges.keys():
                cost = self.distance[j[0]] + self.edges[j] 
                if cost < self.distance[j[1]]:
                    self.distance[j[1]] = cost
                    change = True

            if i != len(self.nodes)-1 and not change:
                print(i)
                for i in self.distance.keys():
                    print("Value for",i,"is",self.distance[i])
                break
            elif i == len(self.nodes)-1:
                print("Negative cycle seen")
        


# Testing

path = os.path.dirname(os.path.abspath(__file__))
values = open( path +'\\bellman.txt','r')

cost,nodes = {},set()
for i in values:
    temp = list(map(int, i.split()))
    cost[(temp[0],temp[1])] = temp[2]
    nodes.add(temp[0]);nodes.add(temp[1])


test = bellmanford( cost,nodes)
test.start(1)       #final all shortest path from the this point