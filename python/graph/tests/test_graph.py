from graph import __version__

from graph.graph import Graphs


def test_version():
    assert __version__ == '0.1.0'


################################################################################

def test_add_node():
    graph = Graphs()
    node_a = graph.add_node('A')

    actual = node_a.value
    expected = 'A'

    assert actual == expected

################################################################################


def test_add_edge():
    graph = Graphs()
    node_a = graph.add_node('A')
    node_b = graph.add_node('B')
    graph.add_Edge(node_a, node_b, 4)

    actual = graph._adjacency_list[node_a][0].node
    expected = node_b

    assert actual == expected

################################################################################


def test_get_nodes():
    graph = Graphs()

    node_a = graph.add_node('A')
    node_b = graph.add_node('B')
    node_c = graph.add_node('C')
    node_d = graph.add_node('D')

    actual = graph.get_nodes()
    expected = ['A', 'B', 'C', 'D']

    assert actual == expected

################################################################################


def test_get_neighbors():
    graph = Graphs()

    node_a = graph.add_node('A')
    node_b = graph.add_node('B')
    node_c = graph.add_node('C')
    node_d = graph.add_node('D')

    graph.add_Edge(node_a, node_b, 4)
    graph.add_Edge(node_a, node_d, 9)
    graph.add_Edge(node_a, node_c, 3)

    actual = graph.get_neighbors(node_a)
    expected = [('B', 4), ('D', 9), ('C', 3)]

    assert actual == expected

################################################################################


def test_size():
    graph = Graphs()

    node_a = graph.add_node('A')
    node_b = graph.add_node('B')
    node_c = graph.add_node('C')
    node_d = graph.add_node('D')

    actual = graph.size()
    expected = 4

    assert actual == expected

################################################################################


def test_size_empty():
    graph = Graphs()

    actual = graph.size()
    expected = 0

    assert actual == expected

################################################################################


def test_graph_with_only_one_node_and_edge():
    graph = Graphs()

    node_a = graph.add_node('A')
    graph.add_Edge(node_a, node_a, 1)

    actual = graph.get_neighbors(node_a)
    expected = [('A', 1)]

    assert actual == expected

################################################################################


def test_empty_graph():
    graph = Graphs()

    actual = graph.get_nodes()
    expected = "null"

    assert actual == expected

################################################################################
