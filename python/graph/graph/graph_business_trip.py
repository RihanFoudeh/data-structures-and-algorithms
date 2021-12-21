from graph.graph import Graphs

################################################################################


def graph_business_trip(graph, arr_city):
    """
    Write a function called business trip
    Determine whether the trip is possible with direct flights, and how much it would cost.
    Arguments: graph, array of city names
    Return: cost or null
    """
    trip = False
    trip_two = False
    cost = 0

    for city_name in range(len(arr_city) - 1):
        edges = graph._adjacency_list[arr_city[city_name]]
        trip_two = False

        for edge in edges:
            if arr_city[city_name + 1] == edge.node:
                cost += edge.weight
                trip = True
                trip_two = True

    trip = trip and trip_two
    # print(trip)
    # print(trip_two)
    if not trip:
        cost = 0
        trip = False
        return f"{trip},${cost}"

    return f"{trip},${cost}"

################################################################################
################################################################################


if __name__ == "__main__":
    graph = Graphs()

    pandora = graph.add_node('Pandora')
    arendelle = graph.add_node('Arendelle')
    metroville = graph.add_node('Metroville')
    monstroplolis = graph.add_node('Monstroplolis')
    narnia = graph.add_node('Narnia')
    naboo = graph.add_node('Naboo')

    graph.add_Edge(pandora, arendelle, 150)
    graph.add_Edge(pandora, metroville, 82)

    graph.add_Edge(arendelle, pandora, 150)
    graph.add_Edge(arendelle, metroville, 99)
    graph.add_Edge(arendelle, monstroplolis, 42)

    graph.add_Edge(metroville, pandora, 82)
    graph.add_Edge(metroville, arendelle, 99)
    graph.add_Edge(metroville, monstroplolis, 105)
    graph.add_Edge(metroville, naboo, 26)
    graph.add_Edge(metroville, narnia, 37)

    graph.add_Edge(monstroplolis, arendelle, 42)
    graph.add_Edge(monstroplolis, metroville, 105)
    graph.add_Edge(monstroplolis, naboo, 73)

    graph.add_Edge(naboo, monstroplolis, 73)
    graph.add_Edge(naboo, metroville, 26)
    graph.add_Edge(naboo, narnia, 250)

    graph.add_Edge(narnia, metroville, 37)
    graph.add_Edge(narnia, naboo, 250)

    print("Neighbors: ")
    print(f"{metroville.value} Neighbors: {graph.get_neighbors(metroville)} \n")

    print("Graph Business Trip: ")
    print(
        f"[Metroville, Pandora, ]: {graph_business_trip(graph, [metroville, pandora,])}")
    print(
        f"[Arendelle, New Monstropolis, Naboo]: {graph_business_trip(graph, [arendelle, monstroplolis, naboo])}")
    print(f"[Naboo, Pandora]: {graph_business_trip(graph, [naboo, pandora])}")
    print(
        f"[Narnia, Arendelle, Naboo]: {graph_business_trip(graph, [narnia, arendelle, naboo])} \n")

    print(
        f"[Pandora, Arendelle, Narnia]: {graph_business_trip(graph, [pandora, arendelle, narnia])}")
    print(
        f"[pandora, arendelle, monstroplolis, naboo, pandora]: {graph_business_trip(graph, [pandora, arendelle, monstroplolis, naboo, pandora])}")
    print(
        f"[pandora, arendelle, monstroplolis, naboo, narnia, metroville, pandora]: {graph_business_trip(graph, [pandora, arendelle, monstroplolis, naboo, narnia, metroville, pandora])}")


################################################################################
