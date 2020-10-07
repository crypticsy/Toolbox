# During implementation of tree in one dimentional array, note:
#       If N denotes the index of parent node then;
#               --> 2N denotes the left child of node
#               --> 2N+1 denotes the right child of node


class heap():

    tree = []

    def choose(this,a,b):   
        return True if this.tree[a-1]<this.tree[b-1] else False   # Minheap
        #return True if this.tree[a]>this.tree[b] else False   # Maxheap


    def heapify(this):      # heap sorts the entire tree
        for i in range(len(this.tree),1,-1):
            parent = i//2
            if this.choose(i,parent):
                this.shift_down(parent)      
    
    def shift_up(this,child):
        while child//2 > 0:
            if this.choose(child,child//2):
                this.tree[child-1],this.tree[child//2-1] = this.tree[child-1], this.tree[child//2-1]
                child = child//2
            else:
                break          

    def shift_down(this,parent):
        while True:
            child1  = 2*parent
            if not child1<=len(this.tree):break
            child2 = child1+1 if child1+1<=len(this.tree) else child1
            swapchild = child1 if this.choose(child1,child2) else child2
            if this.choose(swapchild,parent):
                this.tree[swapchild-1],this.tree[parent-1] = this.tree[parent-1], this.tree[swapchild-1]
                parent = swapchild
            else:
                break

    def generateTree(this,data):    # straight up creating a tree from values
        this.tree = data
        this.heapify()

    def add(this,val):     # for addining values to the tree one by one
        this.tree.append(val)
        this.shift_up(len(this.tree))
    
    def removeTop(this):   #removes the top value and resets the tree
        temp = this.tree[0]
        if len(this.tree)>1:
            this.tree[0] = this.tree.pop()
            this.shift_down(1)
        else:
            this.tree.pop()
        return temp

    def getSize(this):
        return len(this.tree)

'''    
# Testing

temp = heap()

temp.add(1)
temp.add(34)
temp.add(3)
temp.add(4)

for i in range(temp.getSize()):
    print(temp.removeTop())
'''
