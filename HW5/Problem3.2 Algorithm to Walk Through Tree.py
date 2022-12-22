"""
Answer: The algorithm that I am using to walk through each tree and crossing each edge of T
"""


def bfs(visit_complete, graph, current_node):
    visit_complete.append(current_node)
    queue = []
    queue.append(current_node)
    print(f'Queue is {queue}')

    while queue:
        s = queue.pop(0)
        print(s)

        for neighbour in graph[s]:
            if neighbour not in visit_complete:
                visit_complete.append(neighbour)
                queue.append(neighbour)

