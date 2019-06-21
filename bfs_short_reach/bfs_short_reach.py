import collections

def bread_first_search(graph, root):
    visited, queue = set(), collections.deque([root])
    path = []
    while queue:
        vertex = queue.popleft()
        path.append(vertex)
        if graph.get(path[-1]) == []:
            print(path)
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                newpath = path
                newpath.append(neighbour)
                visited.add(neighbour)
                queue.append(neighbour)

if __name__ == "__main__":
    query = int(input())
    for _ in range(query):
        (nodes, edges) = list(map(int, input().split()))
        graph = collections.defaultdict(list)
        for a in range(nodes):
            graph[a] = []
        print(graph)
        for _ in range(edges):
            (src, dest) = list(map(int, input().split()))
            graph[src] = graph.get(src) + [dest]
            start = int(input())
            bread_first_search(graph, start)
        print(graph)
