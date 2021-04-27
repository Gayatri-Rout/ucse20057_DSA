# ucse20057 | Gayatri Rout | DSA assignment 
# find a minimum spanning tree(MST) using Prim's algo from a given graph.

class primAlgo():
    def __init__(x, vertices):
        x.v = vertices
        x.graph = [[0 for col in range(vertices)] 
                      for row in range(vertices)]
    # function to display MST
    def displayMST(x, storeMST):
        print ("Edge \tWeight")
        for i in range(1,x.v):
            print (storeMST[i],"-",i,"\t",x.graph[i][ storeMST[i] ])

    # function to find the vertex with minimum edge weight
    def minWeight(x, key, mstSet):
        positive_infnity = float('inf')
        min = positive_infnity
        for vertex in range(x.v):
            if key[vertex] < min and mstSet[vertex] == False:
                min = key[vertex]
                min_value = vertex
        return min_value

    # creating MST using Prim's algorithm
    def primMST(x):
        positive_infnity = float('inf')
        key = [positive_infnity] * x.v
        storeMST = [None] * x.v # stores the constructed MST
        key[0] = 0   
        mstSet = [False] * x.v
        storeMST[0] = -1  
        for cout in range(x.v):
            u = x.minWeight(key, mstSet)
            mstSet[u] = True
            for V in range(x.v):
                if x.graph[u][V] > 0 and mstSet[V] == False and key[V] > x.graph[u][V]:
                        key[V] = x.graph[u][V]
                        storeMST[V] = u
        x.displayMST(storeMST)

p  = primAlgo(5)
# representation of graph: adjacency matrix
p.graph = [ [0, 7, 8, 1, 0],
             [4, 9, 9, 0, 0],
             [0, 0, 1, 0, 0],
             [2, 8, 0, 0, 9],
             [0, 0, 3, 1, 0],
           ]
p.primMST()

