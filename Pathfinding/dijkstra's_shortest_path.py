class dijkstra_shortest_path():
    graph, distance, final_dist = [{} for x in range(3)]     # attributes
    
    def findmin(self,dict):
        return min(list(dict), key = lambda x:this.final_dist[x])

    def __init__(self, graph, distance):        # initialization
        this.graph, this.distance = graph, distance
        
    def find_path(self, start, end):
        this.final_dist = {x:float('inf') for x in this.graph.keys()}
        visited, inlist = set(), set()

        inlist.add(start)
        this.final_dist[start] = 0

        while inlist != set():
            currkey = this.findmin(inlist)
            visited.add(currkey)
            inlist.discard(currkey)

            for i in this.graph[currkey]:
                if i not in visited:
                    currval = this.final_dist[currkey] + this.distance[(currkey,i)]
                    this.final_dist[i] = min(this.final_dist[i], currval)
                    inlist.add(i)
        
        return this.final_dist[end]