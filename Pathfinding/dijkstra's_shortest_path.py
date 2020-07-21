class dijkstra_shortest_path():

    #attributes
    graph, distance, final_dist = [{} for x in range(3)]

    
    def findmin(this,dict):
        minkey,minval = -1,float('inf')
        for i in list(dict):
            if this.final_dist[i] < minval:
                minkey, minval = i, this.final_dist[i]
        return minkey


    
    # Graph search
    def __init__(this, graph, distance):
        this.graph = graph
        this.distance = distance
        

    def find_path(this, start, end):
        this.final_dist = {x:float('inf') for x in this.graph.keys()}
        visited,inlist = set(),set()
        inlist.add(start)
        this.final_dist[start] = 0

        while inlist!=set():
            currkey = this.findmin(inlist)
            visited.add(currkey)
            inlist.discard(currkey)

            for i in this.graph[currkey]:
                if i not in visited:
                    currval = this.final_dist[currkey] + this.distance[(currkey,i)]
                    this.final_dist[i] = min(this.final_dist[i],currval)
                    inlist.add(i)
        
        return this.final_dist[end]
            
                



 #Testing

values = open('d:/Learning/Stanford Algo Class/2. Graph Search, Shortest Paths, and Data Structures/dijkstraData.txt','r')

tempgraph, tempdist = {},{}
for i in values:
    val = i.split()
    
    node1 = val.pop(0) 
    tempgraph.setdefault(node1,[])
    for a in val:
        node2,dist = a.split(',')
        tempgraph[node1].append(node2)
        tempdist[(node1,node2)] = int(dist)
    

test1 = dijkstra_shortest_path(tempgraph,tempdist)
start = '1'


for i in [7,37,59,82,99,115,133,165,188,197]:
    print("Shortest distance from",start,"to",i,"is  : ",test1.find_path(start,str(i)))
