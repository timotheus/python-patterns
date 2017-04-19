

class DFS(object):

    def __init__(self, graph):
        self._graph = graph

    def traverse(self, start_node):
        visited, stack = [], [start_node]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                for nextNode in self._graph[node]:
                    if nextNode not in visited:
                        stack.append(nextNode)
        return visited
