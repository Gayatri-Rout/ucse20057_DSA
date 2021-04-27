# ucse20057 | Gayatri Rout | DSA assignment 
# Dijkstra’s Shortest Path ALgo
class Graph:
    def __init__(self):
        self.vertices = {}
 
    # adding a vertex with the given key to the graph
    def add_v(self, key):
        vertex = Vertex(key)
        self.vertices[key] = vertex
 
    # returning vertex object with the corresponding key
    def get_v(self, key):
        return self.vertices[key]
 
    def __contains__(self, key):
        return key in self.vertices
 
    # adding an edge from src_key to dst_key with given weight
    def add_e(self, src_key, dst_key, wgt = 1):
        self.vertices[src_key].add_neighbour(self.vertices[dst_key], wgt)
 
    # returning True if there is an edge from src_key to dst_key
    def does_e_exist(self, src_key, dst_key):
        return self.vertices[src_key].does_it_point_to(self.vertices[dst_key])
 
    def __iter__(self):
        return iter(self.vertices.values())
 
 
class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}
 
    # returing key corresponding to this vertex object.
    def get_key(self):
        return self.key
 
    # making this vertex point to dest with given edge weight
    def add_neighbour(self, dst, wgt):
        self.points_to[dst] = wgt
 
    # returning all vertices pointed to by this vertex
    def get_neighbours(self):
        return self.points_to.keys()
    
    # getting the weight of edge from this vertex to dst
    def get_weight(self, dst):
        return self.points_to[dst]
    
    # returning True if this vertex points to dst
    def does_it_point_to(self, dst):
        return dst in self.points_to
 
# function to find shortest path using Dijkstra’s algo
def dijkstraAlgo(g, source):
    unvisited_list = set(g)
    dist = dict.fromkeys(g, float('inf'))
    dist[source] = 0
 
    while unvisited_list != set():
        closest = min(unvisited_list, key=lambda v: dst[v])
        unvisited_list.remove(closest)
        for neighbour in closest.get_neighbours():
           if neighbour in unvisited_list:
               new_dist = dist[closest] + closest.get_weight(neighbour)
               if dist[neighbour] > new_dist:
                   dist[neighbour] = new_dist
 
    return dist
 
 
g = Graph()
print("\nUNDIRECTED GRAPGH")
print("-----------------")
n = 0
while n != 5:
    print("\nMENU")
    print("-----------------")
    print("(press 1) Add vertex")
    print("(press 2) Add edge")
    print("(press 3) Shortest")
    print("(press 4) Display")
    print("(press 5) Quit")
    n = int(input("\nWhat would you like to do? "))
    if n == 1:
        print("\nADD VERTEX: ")
        print("-----------------")
        key = int(input("Key? "))
        if key not in g:
                g.add_v(key)
        else:
            print('Vertex already exists.')
    elif n == 2:
        print("\nADD EDGE: ")
        print("-----------------")
        src = int(input("Source? "))
        dst = int(input("Destination? "))
        wgt = int(input("Weight? "))
        if src not in g:
                print('\nVertex {} does not exist.'.format(src))
        elif dst not in g:
            print('\nVertex {} does not exist.'.format(dst))
        else:
            if not g.does_e_exist(src, dst):
                g.add_e(src, dst, wgt)
                g.add_e(dst, src, wgt)
            else:
                print('\nEdge already exists.')
    elif n == 3:
        print("\nSHORTEST: ")
        print("-----------------")
        key = int(input("Source vertex key? "))
        source = g.get_v(key)
        distance = dijkstraAlgo(g, source)
        print('\nDistances from {}: '.format(key))
        for v in distance:
            print('\nDistance to {}: {}'.format(v.get_key(), distance[v]))
        print()
    
    elif n == 4:
        print("\nDISPLAY: ")
        print("-----------------")
        print('Vertices: ', end= "")
        for v in g:
            print(v.get_key(), end= " ")
        print()
 
        print('Edges: ')
        for v in g:
            for dest in v.get_neighbours():
                w = v.get_weight(dst)
                print("Source={0}, Destination={1}, Weight={2}".format(v.get_key(), dst.get_key(), w))
        print()
    
    else:
        print("\nIncorrect Input!\nTRY AGAIN!!")
print("\n------------PROGRAM TERMINATED :)------------\n") 
   
          

 
