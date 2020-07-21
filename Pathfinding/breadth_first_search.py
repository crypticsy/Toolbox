def bfs(start, graph):
    queue = [start]
    seen = {start}
    paths = {start:[start]}

    while len(queue)>0:
        current = queue.pop(0)
        currlist = paths[current]

        for neighbor in graph[current]:
            if neighbor not in seen:
                seen.add(neighbor)
                paths[neighbor] = currlist + [neighbor]
                queue.append(neighbor)
    
    return paths


'''
#Test

data = {1:[23,4,5],23:[1,2],2:[23],4:[1,7],5:[1],7:[4]}
mybase = 23

pathways = {}
for i in data.keys():
	if i not in pathways:
		pathways[i] = bfs(i,data)

print(pathways)
'''
