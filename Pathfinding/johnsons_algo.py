import os



class johnson:
    edgecost, nodelinks, final_dist, allnodes, alteredvalues  = {}, {}, {}, set() , None


    def findmin(self,dict): return min(list(dict), key = lambda x:self.final_dist[x])

    def __init__(self, cost, nodes):
        distance = {'temp':0}
        for i in nodes:
            cost[('temp',i)] = 0
            distance[i] = float('inf')

        for i in range(len(nodes)):         # Run belman ford algorithm once
            change = False

            for j in cost.keys():
                curcost = distance[j[0]] + cost[j] 
                if curcost < distance[j[1]]:
                    distance[j[1]] = curcost
                    change = True

            if i != len(nodes)-1 and not change:break
            elif i == len(nodes)-1:print("Negative cycle found")


        for i in cost.keys():
            if i[0] != "temp":
                self.edgecost[(i[0], i[1])] = distance[i[0]] + cost[i] - distance[i[1]]
                self.nodelinks.setdefault(i[0],[]).append(i[1])
                
        self.allnodes = nodes
        self.alteredvalues = distance
        print(self.edgecost)

    
    def find_path(self, start):
        self.final_dist = {x:float('inf') for x in self.allnodes}       # run dijkstra's shortest path algorithm in the new graph
        visited, inlist = set(), set()

        inlist.add(start)
        self.final_dist[start] = 0
        parent = {start : []}

        while inlist != set():
            currkey = self.findmin(inlist)
            visited.add(currkey)
            inlist.discard(currkey)

            if currkey in self.nodelinks:
                for i in self.nodelinks[currkey]:
                    if i not in visited:
                        currval = self.final_dist[currkey] + self.edgecost[(currkey,i)]
                        if currval < self.final_dist[i]:
                            self.final_dist[i], parent[i] = currval, parent[currkey] + [i]
                        inlist.add(i)
        

        actualdist = {}
        for i in self.final_dist.keys():        # return the total cost back to their original values
            actualdist[i] = self.final_dist[i] - self.alteredvalues[start] + self.alteredvalues[i]
        
        return parent, actualdist       # returns all paths and cost from source vertex to all the other nodes in the graph


        



path = os.path.dirname(os.path.abspath(__file__))
values = open( path +'\\johnson.txt','r')

cost,nodes = {},set()
for i in values:
    temp =  i.split()
    cost[(temp[0],temp[1])] = int(temp[2])
    nodes.add(temp[0]);nodes.add(temp[1])

test = johnson( cost,nodes)
t1, t2 = test.find_path('a')
print(t1, t2)