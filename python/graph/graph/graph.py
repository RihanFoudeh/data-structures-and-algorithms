class Node():

    def __init__(self, value):
        self.value = value


    def __str__(self):
        return str(self.value)



class Edge():
    def __init__(self, node, weight=1):
        self.node = node
        self.weight = weight



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
        """
        Adds a new edge between two nodes in the graph
        If specified, assign a weight to the edge
        Both nodes should already be in the Graph
        Arguments: 2 nodes to be connected by the edge, weight (optional)
        Returns: nothing
        """
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


        return str

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

################################################################################
