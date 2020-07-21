class point():
    def __init__(self,x,y):self.x,self.y = x,y

def distance(p1,p2):
    return ((p2.x - p1.x)**2 + (p2.y - p1.y)**2 )**(1/2)

def brute(data, n): 
    min_val = float('inf')  
    for i in range(n): 
        for j in range(i + 1, n): 
            dist = distance(data[i], data[j])
            if dist < min_val:min_val = dist
    return min_val 

def closest(data,size):
    if size<=3:return brute(data, size)
    
    mid = size//2  #mid point
    midPoint = data[mid]

    cleft = closest(data[:mid], mid) 
    cright = closest(data[mid:], size - mid) 
    minD = min(cleft, cright) 

    strip = []      #for the points that lie in between minD from midpoint
    for i in range(size):  
        if abs(data[i].x - midPoint.x) < minD:strip.append(data[i]) 
    return min(minD,brute(strip, len(strip)))

def manhattansort(data):
    data.sort(key = lambda point:point.x)
    return closest(data,len(data))

'''
# Testing 
data = []
for i in range(int(input())):
      x,y = map(int, input().split())
      data.append(point(x,y))

print(manhattansort(data))
'''
