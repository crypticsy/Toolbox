def floodfill(x,y,grid,height,width):
    seen = {}
    currhead = [(x,y)]

    while currhead != []:
        val = currhead.pop(0)
        for i in [(0,1),(0,-1),(1,0),(-1,0)]:   #for diagonals add (-1,-1),(1,1),(-1,1),(1,-1)
            tmpx,tmpy = val[0]+i[0],val[1]+i[1]
            
            if tmpx>-1 and tmpy>-1 and tmpy<height and tmpx<width and (tmpx,tmpy not in seen):
                currhead.append((tmpx,tmpy)) 
                seen[(tmpx,tmpy)] = None
