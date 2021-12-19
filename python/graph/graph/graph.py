from graph.stack_and_queue import Stack, Queue


################################################################################

class Node():

    def __init__(self, value):
        self.value = value

    #########################################################

    def __str__(self):
        return str(self.value)

################################################################################


class Edge():
    def __init__(self, node, weight=1):
        self.node = node
        self.weight = weight

################################################################################


class Graphs():

    def __init__(self):
        self._adjacency_list = {}

    #########################################################

    def add_node(self, value):
        """
        Add a node to the graph
        Arguments: value
        Returns: The added node
        """
        node = Node(value)
        self._adjacency_list[node] = []
        return node

    #########################################################

    def add_Edge(self, node1, node2, weight=1):

        if node1 and node2 in self._adjacency_list:
            self._adjacency_list[node1].append(Edge(node2, weight))

    #########################################################

    def get_nodes(self):
        """
        Returns all of the nodes in the graph as a collection (set, list, or similar)
        Arguments: none
        """
        if self._adjacency_list:
            return [key.value for key in self._adjacency_list]
        else:
            return 'null'

        # list = []
        # if self._adjacency_list.keys():
        #     for node in self._adjacency_list.keys():
        #         list.append(node.__str__())
        #     return list
        # else:
        #     return 'NULL'

    #########################################################

    def get_neighbors(self, node):
        """
        Returns a collection of edges connected to the given node
        Include the weight of the connection in the returned collection
        get neighbors
        Arguments: node
        """
        return [(edge.node.value, edge.weight) for edge in self._adjacency_list[node]]

    #########################################################

    def size(self):
        """
        Returns the total number of nodes in the graph
        Arguments: none
        """
        return len(self._adjacency_list)

    #########################################################

    def __str__(self):
        str = ''
        for node in self._adjacency_list:
            str += f'[{node.value}] -> {self.get_neighbors(node)}\n'

            # str += f'[{node.value}] -> '

            # for edge in self._adjacency_list[node]:
            #     str += f" ( {edge.node.value}, {edge.weight} ), "
            # str += '\n'

        return str

    #########################################################

    def breadth_first(self, node):
        """
        Write the following method for the Graph class:
        breadth first
        Arguments: Node
        Return: A collection of nodes in the order they were visited.
        Display the collection
        """
        if node not in self._adjacency_list:
            return 'Node does not in Graph'
        elif self._adjacency_list[node]==[]:
            return 'Node does not have neighbors'

        breadth = Queue()
        visited = []
        nodes = []

        breadth.enqueue(node)
        visited.append(node)

        while breadth.front:
            front = breadth.dequeue()
            nodes.append(front.value)

            for child in self._adjacency_list[front]:

                if child.node not in visited:
                    visited.append(child.node)
                    breadth.enqueue(child.node)

        return nodes

################################################################################
################################################################################


if __name__ == "__main__":
    graph = Graphs()

    node_a = graph.add_node('A')
    node_b = graph.add_node('B')
    node_c = graph.add_node('C')
    node_d = graph.add_node('D')

    graph.add_Edge(node_a, node_a, 1)

    graph.add_Edge(node_a, node_b, 4)
    graph.add_Edge(node_a, node_d, 9)
    graph.add_Edge(node_a, node_c, 3)

    graph.add_Edge(node_b, node_a, 4)
    graph.add_Edge(node_b, node_d, 5)

    graph.add_Edge(node_c, node_a, 3)
    graph.add_Edge(node_c, node_d, 6)

    graph.add_Edge(node_d, node_a, 9)
    graph.add_Edge(node_d, node_b, 5)
    graph.add_Edge(node_d, node_c, 6)

    print("Get Nodes :")
    print(graph.get_nodes())

    print("Get Neighbors :")
    print(graph.get_neighbors(node_a))
    print(graph.get_neighbors(node_b))
    print(graph.get_neighbors(node_c))
    print(graph.get_neighbors(node_d))

    print("Size :")
    print(graph.size())

    print("Str :")
    print(graph)

    print("Breadt First:")
    print(graph.breadth_first(node_a))
    #########################################################

    graph2 = Graphs()

    pandora = graph2.add_node('Pandora')
    arendelle = graph2.add_node('Arendelle')
    metroville = graph2.add_node('Metroville')
    monstroplolis = graph2.add_node('Monstroplolis')
    narnia = graph2.add_node('Narnia')
    naboo = graph2.add_node('Naboo')

    fake = graph.add_node('Fake')
    fake2 = graph2.add_node('Fake 2')

    graph2.add_Edge(pandora, arendelle, 1)

    graph2.add_Edge(arendelle, metroville, 1)
    graph2.add_Edge(arendelle, monstroplolis, 1)

    graph2.add_Edge(metroville, arendelle, 1)
    graph2.add_Edge(metroville, monstroplolis, 1)
    graph2.add_Edge(metroville, narnia, 1)
    graph2.add_Edge(metroville, naboo, 1)


    graph2.add_Edge(monstroplolis, arendelle, 1)
    graph2.add_Edge(monstroplolis, metroville, 1)
    graph2.add_Edge(monstroplolis, arendelle, 1)

    graph2.add_Edge(narnia, metroville, 1)
    graph2.add_Edge(narnia, naboo, 1)

    graph2.add_Edge(naboo, monstroplolis, 1)
    graph2.add_Edge(naboo, metroville, 1)
    graph2.add_Edge(naboo, narnia, 1)


    print("Breadt First:")
    print(graph2.breadth_first(pandora))

################################################################################
