class Graph:
    def __init__(self,node=None):
        self.nodes=node or {}
    def bfs(self,start,goal):
        queue=[[start]]
        visited=[]
        if start==goal:
            return 'That was easy! Start = goal'
        while queue:
            s=queue.pop(0)
            node=s[-1]
            print(node)
            if node not in visited:
                neighbours=self.nodes[node]
                for neighbour in neighbours:
                    path=list(s)
                    path.append(neighbour)
                    queue.append(path)
                    if neighbour==goal:
                        return s
                visited.append(node)
        return 'sorry path Not found'
g = {'A': ['B', 'C', 'E'],
         'B': ['A','D', 'E'],
         'C': ['A', 'F', 'G'],
         'D': ['B'],
         'E': ['A', 'B','D'],
         'F': ['C'],
         'G': ['C']}
gra=Graph(g)
print(gra.bfs('G','D'))
