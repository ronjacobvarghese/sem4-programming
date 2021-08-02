
def bfs(visited, graph, node):

    visited.append(node)
    queue.append(node)

    while queue:
        rmv = queue.pop(0)
        print (rmv, end = " ")

        for i in graph[rmv]:
            if i not in visited:
                visited.append(i)
                queue.append(i)


def dfs(graph, node):

    stack = []
    path = []

    stack.append(node)

    while stack:
        v = stack.pop()

        if v in path:
            continue

        path.append(v)
        print(v,end = " ")


        for i in graph:
            stack.append(i)

    return path




graph = {
  '0' : ['1','3'],
  '1' : ['0','2','3','5','6'],
  '2' : ['1','3','4','5'],
  '3' : ['0','1','2','4'],
  '4' : ['2','3','6'],
  '5' : ['1','2'],
  '6' : ['1','4']
}


visited = []
queue = []

print("\nElements traversed using Breadth-First Search")
bfs(visited, graph, '0')
print("\n")


print("\nElements traversed using Depth-First Search")
dfs(graph, '0')
print("\n")
