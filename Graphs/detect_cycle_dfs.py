graph,nodes = {},set()


# --- Testing ---- 
n = 3
val = ['A > B', 'B > C', 'A > C' ]      # data

for i in range(n):
    row = val[i].replace(" ","").split(">")
    graph.setdefault(row[0],[]).append(row[1])
    nodes.add(row[0])
    nodes.add(row[1])


using, seen = set(),set()
def checkCycle(a):
    using.add(a)
    if a in graph:      # if the current node has neighbors
        for neighbor in graph[a]:
            if neighbor in using: return True       # if cycle is detected return True
            elif neighbor not in seen and neighbor not in using:
                if checkCycle(neighbor): return True        # if cycle was detected from it's neighbor return True
        
    using.discard(a)
    seen.add(a)
    return False

def check():
    for i in nodes:
        if i not in seen:
            if checkCycle(i):return False       # if cycle was detected from it's neighbor return False
    return True



print("No cycle was detected" if check() else "Cycle was detected")