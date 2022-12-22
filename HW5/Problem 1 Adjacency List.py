# this is the algorithm that would give linear time

def reverse_directed_graph(directed_graph: dict) -> dict:
    """
    Reverse directed graph using adjacency matrix. For adjacency matrix, we are implemented that using a dictionary
    with node as the dictionary key and all the connected edges in the set of list.
    :return: new reverse graph
    :rtype: dictionary
    """
    new_reversed_graph = {}
    # loop through each node in the directed graph
    for nodes in directed_graph:
        # loop through each child not in the directed graph
        for child_nodes in directed_graph[nodes]:
            # if nodes and child node is not in reversed graph, add it as a key
            if nodes not in new_reversed_graph:
                new_reversed_graph[nodes] = set([])
            if child_nodes not in new_reversed_graph:
                new_reversed_graph[child_nodes] = set([])

            # append child nodes to the new reversed graph
            if child_nodes in directed_graph:
                new_reversed_graph[child_nodes].add(nodes)

    return new_reversed_graph


if __name__ == '__main__':
    graph1 = {1: set([3, 5]),
              2: set([4, 1]),
              3: set([4]),
              4: set([5]),
              5: set([])
              }
    graph2 = {'a': set(['c', 'b', 'd']),
              'b': set(['d']),
              'c': set(['d', 'e']),
              'd': set(['e']),
              'e': set(['a'])
              }
    g1 = reverse_directed_graph(graph1)
    g2 = reverse_directed_graph(graph2)
    print(f'g1: {graph1}\n --> reverse = {g1}\n')
    print(f'g2: {graph2}\n --> reverse = {g2}\n')

