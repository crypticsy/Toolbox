def CreateClusters(cost):
    order = sorted(cost.keys(), key = lambda x:cost[x])
    numOfClusters = 4
    
    tree,group,gcount = {},{},0

    while order!=[]:
        i = order.pop(0)

        if i[0] not in tree and i[1] not in tree:       #When the nodes aren't in any group
            tree[i[0]],tree[i[1]] = gcount,gcount
            group[gcount] = [i[0],i[1]]
            gcount+=1


        elif i[0] not in tree or i[1] not in tree:                  #when one of the node is in a group
            temp, tempo = (tree[i[1]],i[0]) if i[0]not in tree else (tree[i[0]],i[1]) 
            tree[tempo] = temp
            group[temp].append(tempo)


        elif tree[i[0]] != tree[i[1]]:                  #when both nodes are in different groups
            g1,g2 = tree[i[0]],tree[i[1]]
            min_node_key = g1 if len(group[g1])<len(group[g2]) else g2
            max_node_key = g1 if min_node_key != g1 else g2

            for i in group[min_node_key]:
                tree[i] = max_node_key
            group[max_node_key]+= group[min_node_key]
            group.pop(min_node_key)

        if len(group) + total - len(tree) == numOfClusters:
            break


    print("Current groups of clusters : ",group.keys(),file =sys.stderr)

    temp = [i for i in order if i[0] not in tree or i[1] not in tree or tree[i[0]] != tree[i[1]]]
    print("Max spacing between the clusters : ", cost[temp[0]])
