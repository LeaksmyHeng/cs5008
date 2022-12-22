"""
----------------------------------------- Problem1.2 -----------------------------------------
The overall time complexity to build the word ladder graph could be done in O(n^2) or specifically O(kn^2)
where n is the number of word and k is the length of the word. To do so, first we are going to assume that
each words have the same length and the starting point is already in the word list.
Implementation:
    - Start by creating a vertex in the graph for every word in the list -> O(n)
    - Compare each word in the list with others: -> O(n)
        - Comparing by checking how many letters are different -> O(k)
            - If there are more than one letter difference, no edges between those two node
            - If there is exactly one letter different, there is an edge between those two nodes
Hence, the overall time complexity for this is O(kn^2).
Please see code below create_graph(wordlist: list) & is_adjancency(word1, word2)


----------------------------------------- Problem1.3 -----------------------------------------
As we know from problem 1.2, to convert the word list to a graph, it takes O(kn^2) time. So now, we
are going to use that graph to check for the shortest path from startword to endword (example, startword and
endword is 'hit' and 'cog' respectively). To implement that, we are going to use BFS or breath first search.
Implementation:
    - Start by creating an empty queue and empty visited_node (both are list and queue will be used to
    maintain the path whereas visited_node will be use to keep track of the nodes that we have already visited)
    - loop through the queue to check if the node aka the first word is the same as the endword. -> O(n)
        - If it is return the path
        - else:
            - loop through the adjacency list or neighboring node. -> O(n)
            - If we have not visited that neighboring node yet, add that to the visited_node list. -> O(n)
Based on this implementation, the algorithm takes O(n^3).
In total, converting the word list to graph representation then implementing BFS on top of that takes
O(n^3 + kn^2)
Please see code below word_ladder(startword: str, endword: str, wordlist: list)
"""


def is_adjancency(word1, word2):
    """
    This is to compare each word.
    :param word1: str the first word that we want to compare
    :param word2: str the second word that we want to compared
    :return: return true if there is exactly one letter difference aka the two word is adjacent to one another

    This checking take O(k) time where is is the length of the word.
    """
    counter = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            counter += 1
    if counter == 1:
        return True

    return False


def create_graph(wordlist: list):
    """
    Function to create a graph.
    :param wordlist: a list that contains of words
    :return: A dictionary with node or str as a key and their neighboring node in a list as a value
    Example: {'hit': ['hot'], 'cog': ['dog', 'log'], 'hot': ['hit', 'dot', 'lot'], 'dot': ['hot', 'dog', 'lot'], 'dog': ['cog', 'dot', 'log'], 'lot': ['hot', 'dot', 'log'], 'log': ['cog', 'dog', 'lot']}

    This algorithm takes O(n^2 * k) because we loop through each words twice to compare it with one another.
    So it takes O(n^2) then we compare each letter through is_adjeancency function. It takes O(k).
    In total, it takes O(kn^2) time complexity
    """
    dictionary = {}
    for i in wordlist:
        for j in wordlist:
            if is_adjancency(i, j):
                if i not in dictionary:
                    dictionary[i] = []
                    dictionary[i].append(j)
                else:
                    dictionary[i].append(j)

    return dictionary


def word_ladder(startword: str, endword: str, wordlist: list):
    """
    Function to return the shortest path using BFS.
    :param startword: str the start node
    :param endword: str the end node
    :param wordlist: list of words
    :return: the minimum number of steps to convert word
    """
    graph = create_graph(wordlist)
    queue = []
    visited_node = []
    queue.append([startword])
    visited_node.append(startword)

    while queue:
        path = queue.pop(0)
        node = path[-1]
        #print(path, queue, node)
        if str(node).lower() == str(endword).lower():
            min_number_of_steps = len(path)
            print(path)
            return min_number_of_steps

        for adjacent in graph.get(node, []):
            # keep track of visited nodes
            if adjacent not in visited_node:
                visited_node.append(adjacent)
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)


print(word_ladder('hit', 'cog', ['hit', 'cog', 'hot', 'dot', 'dog', 'lot', 'log']))
