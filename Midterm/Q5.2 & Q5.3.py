"""
Q5.2
Explanation:
    First we will sort the node in a descending order of degree. Then color the first vertex in the list.
    Then go down the sorted list and color each nodes (neightbor node) that are not connected the the colored node
    and we will repeat that process.

Runtime: O(n^2) because we loop through each of the nodes at E edges to go through all the neghbors.
"""


def coloring_greedy(graph: dict):
    """
    A greedy algorithm to get the minimum number of color in a graph.
    :param graph:a dictionary that the key is a node, and the value is the list of its neighboring node. For graph, you
    need to list all vertices and its neighbor.
    :type graph: dictionary
    :return: a dictionary that the key is the color, and the value is the node associated with the color
    :rtype: dict
    """
    # sorted the node in a descending order of degree
    nodes = sorted(graph, key=lambda x: len(graph[x]), reverse=True)
    return_graph = {}

    # loop through every nodes to get each node
    for node in nodes:
        # create a color list that has True as per every element in there
        # and the number of element is the number of nodes
        color_lists = len(nodes) * [True]
        # loop through to get all the neighboring_node
        for neighboring_node in graph[node]:
            # if the neighboring node is in the return_graph
            # mark the color_lists element in that position of the neighboring_node to False
            print(f"1. node: {node}'s neighboring node is {neighboring_node}")
            if neighboring_node in return_graph:
                color_lists[return_graph[neighboring_node]] = False
                print(f"2. Mark the color list at position {return_graph[neighboring_node]} to false")
        # use enumerate to get the index number (index number is the same as coloring number)
        # and to access the element in unused_color
        print(f"node: {node} has color list of {color_lists}")
        for color_index in enumerate(color_lists):
            # color_index[1] is the element in the color_list list
            # so as long as the element in the position is true, we mark the node to that index color
            # use break so that we don't have to loop through any more after reassigned the node to the color to
            # avoid using high coloring number
            print(f"3. The color index is {color_index[0]} with value {color_index[1]}")
            if color_index[1]:
                return_graph[node] = color_index[0]
                print(f"4. mark node {node} to color index {color_index[0]}")
                break

    return return_graph


################################################################################################
# Q5.3 Apply algorithm to the graph
graph = {'a': ['b', 'e', 'f', 'd'],
         'f': ['g', 'a', 'k'],
         'g': ['c', 'e', 'h', 'i', 'f'],
         'h': ['b', 'g', 'k'],
         'i': ['g', 'd', 'j'],
         'j': ['b', 'e', 'i', 'k'],
         'b': ['c', 'j', 'a', 'h'],
         'c': ['b', 'd', 'g'],
         'd': ['c', 'a', 'i', 'k'],
         'e': ['a', 'g', 'j'],
         'k': ['d', 'f', 'h', 'j']
         }
# calling the function and the step by step explanation will be in the execution
# microsoft word file will be attach for the result of the code and a description in there as well
# in total there are 4 colors chosen: color 0,1,2,3
print(coloring_greedy(graph))

########################################################################################################################
# Q5.4 Apply algorithm to the graph
# counter example of the graph is below
# with this counter example, the algorithm said to used 3 color but we could do 2 here.
g1 = {'a': ['x'],
      'b': ['x'],
      'c': ['x'],
      'd': ['x'],
      'x': ['b', 'd', 'c', 'a'],
      'e': ['x', 'f', 'g'],
      'f': ['e'],
      'g': ['e', 'h'],
      'h': ['g', 'i', 'j', 'k', 'l', 'm'],
      'i': ['h'],
      'j': ['h'],
      'k': ['h'],
      'l': ['h'],
      'm': ['h']}
print(coloring_greedy(g1))
