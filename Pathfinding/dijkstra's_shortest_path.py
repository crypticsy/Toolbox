class dijkstra_shortest_path():
    graph, distance, final_dist = {},{},{}    # attributes

    def __init__(this, graph, distance): this.graph, this.distance = graph, distance
    
    def findmin(this,dict): return min(list(dict), key = lambda x:this.final_dist[x])
        
    def find_path(this, start):
        this.final_dist = {x:float('inf') for x in this.graph.keys()}
        visited, inlist = set(), set()

        inlist.add(start)
        this.final_dist[start] = 0
        parent = {start : []}

        while inlist != set():
            currkey = this.findmin(inlist)
            visited.add(currkey)
            inlist.discard(currkey)

            for i in this.graph[currkey]:
                if i not in visited:
                    currval = this.final_dist[currkey] + this.distance[(currkey,i)]
                    if currval < this.final_dist[i]:
                        this.final_dist[i], parent[i] = currval, parent[currkey] + [i]
                    inlist.add(i)
        
        return parent, this.final_dist
