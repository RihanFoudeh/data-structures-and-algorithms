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
################################################################################
################################################################################




def test_breadth_first():
    graph = Graphs()

    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    metroville = graph.add_node('Metroville')
    monstroplolis = graph.add_node('Monstroplolis')
    narnia = graph.add_node('Narnia')
    naboo = graph.add_node('Naboo')

    graph.add_Edge(pandora, arendelle, 1)
    graph.add_Edge(arendelle, metroville, 1)
    graph.add_Edge(arendelle, monstroplolis, 1)
    graph.add_Edge(metroville, arendelle, 1)
    graph.add_Edge(metroville, monstroplolis, 1)
    graph.add_Edge(metroville, narnia, 1)
    graph.add_Edge(metroville, naboo, 1)
    graph.add_Edge(monstroplolis, arendelle, 1)
    graph.add_Edge(monstroplolis, metroville, 1)
    graph.add_Edge(monstroplolis, arendelle, 1)
    graph.add_Edge(narnia, metroville, 1)
    graph.add_Edge(narnia, naboo, 1)
    graph.add_Edge(naboo, monstroplolis, 1)
    graph.add_Edge(naboo, metroville, 1)
    graph.add_Edge(naboo, narnia, 1)

    actual = graph.breadth_first(pandora)
    expected = ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']

    assert actual == expected

################################################################################

def test_breadth_first_two():
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

    actual = graph.breadth_first(node_a)
    expected = ['A', 'B', 'D', 'C']

    assert actual == expected

################################################################################

def test_breadth_first_node_not_in_graph():
    graph = Graphs()

    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    metroville = graph.add_node('Metroville')
    monstroplolis = graph.add_node('Monstroplolis')
    narnia = graph.add_node('Narnia')
    naboo = graph.add_node('Naboo')

    graph.add_Edge(pandora, arendelle, 1)
    graph.add_Edge(arendelle, metroville, 1)
    graph.add_Edge(arendelle, monstroplolis, 1)
    graph.add_Edge(metroville, arendelle, 1)
    graph.add_Edge(metroville, monstroplolis, 1)
    graph.add_Edge(metroville, narnia, 1)
    graph.add_Edge(metroville, naboo, 1)
    graph.add_Edge(monstroplolis, arendelle, 1)
    graph.add_Edge(monstroplolis, metroville, 1)
    graph.add_Edge(monstroplolis, arendelle, 1)
    graph.add_Edge(narnia, metroville, 1)
    graph.add_Edge(narnia, naboo, 1)
    graph.add_Edge(naboo, monstroplolis, 1)
    graph.add_Edge(naboo, metroville, 1)
    graph.add_Edge(naboo, narnia, 1)

    graph2 = Graphs()
    fake = graph2.add_node('Fake')

    actual = graph.breadth_first(fake)
    expected = 'Node does not in Graph'

    assert actual == expected

################################################################################

def test_breadth_first_node_does_not_have_neighbors():
    graph = Graphs()

    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    metroville = graph.add_node('Metroville')
    monstroplolis = graph.add_node('Monstroplolis')
    narnia = graph.add_node('Narnia')
    naboo = graph.add_node('Naboo')
    fake = graph.add_node('Fake')

    graph.add_Edge(pandora, arendelle, 1)
    graph.add_Edge(arendelle, metroville, 1)
    graph.add_Edge(arendelle, monstroplolis, 1)
    graph.add_Edge(metroville, arendelle, 1)
    graph.add_Edge(metroville, monstroplolis, 1)
    graph.add_Edge(metroville, narnia, 1)
    graph.add_Edge(metroville, naboo, 1)
    graph.add_Edge(monstroplolis, arendelle, 1)
    graph.add_Edge(monstroplolis, metroville, 1)
    graph.add_Edge(monstroplolis, arendelle, 1)
    graph.add_Edge(narnia, metroville, 1)
    graph.add_Edge(narnia, naboo, 1)
    graph.add_Edge(naboo, monstroplolis, 1)
    graph.add_Edge(naboo, metroville, 1)
    graph.add_Edge(naboo, narnia, 1)

    actual = graph.breadth_first(fake)
    expected = 'Node does not have neighbors'

    assert actual == expected

################################################################################
