# ucse20057 | Gayatri Rout | DSA assignment 

# representation of graph: adjacency list
graph = {
    'A' : ['B', 'C'],
    'B' : ['D', 'A'],
    'C' : ['A', 'B', 'D'],
    'D' : ['C']
}

visited_list_dfs = set() # keeping a track of visited nodes (dfs).

# function to implement DFS
def dfs(visited_list_dfs, graph, s_node):
    if s_node not in visited_list_dfs:
        print(s_node, end = " ")
        visited_list_dfs.add(s_node)
        for neighbour in graph[s_node]:
            dfs(visited_list_dfs, graph, neighbour)

queue = []
visited_list_bfs = []
# function to implement BFS
def bfs(visited_list_bfs, graph, s_node):
  visited_list_bfs.append(s_node)
  queue.append(s_node)

  while queue:
    element = queue.pop(0) 
    print (element, end = " ") 

    for neighbour in graph[element]:
      if neighbour not in visited_list_bfs:
        visited_list_bfs.append(neighbour)
        queue.append(neighbour)


# printing DFS & BFS of given graph
n = 0
while n != 3:
    n = int(input("\n\nDFS Traversal(press 1)\nBFS Traversal(press 2)\nQuit(press 3)\n\nWhat to do? "))
    if n == 1:
        print("\nDFS Graph Traversal:")
        s_node = str(input("Source node out of [ A, B, C, D] ? "))
        dfs(visited_list_dfs, graph, s_node.upper())

    elif n == 2:
        print("\nBFS Graph Traversal:")
        s_node = str(input("Source node out of [ A, B, C, D] ? "))
        bfs(visited_list_bfs, graph, s_node.upper())
    
    else:
        print("\nIncorrect Input!\nTRY AGAIN")

print("\n------------PROGRAM TERMINATED :)------------\n")