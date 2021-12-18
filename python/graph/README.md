# Graphs
<!-- Short summary or background information -->
## A graph is a non-linear data structure that can be looked at as a collection of vertices (or nodes) potentially connected by line segments named edges

## PR Description Section

| Table Of Content              | Links                                                                                                |
| ----------------------------- | ---------------------------------------------------------------------------------------------------- |
| PR '1' > Graph Implementation | [PR '1' > Graph]() |

## Challenge
<!-- Description of the challenge -->
### Features

> Implement your own Graph. The graph should be represented as an adjacency list, and should include the following methods:

* add node
  * Arguments: value
  * Returns: The added node
  * Add a node to the graph
* add edge
  * Arguments: 2 nodes to be connected by the edge, weight (optional)
  * Returns: nothing
  * Adds a new edge between two nodes in the graph
  * If specified, assign a weight to the edge
  * Both nodes should already be in the Graph
* get nodes
  * Arguments: none
  * Returns all of the nodes in the graph as a collection (set, list, or similar)
* get neighbors
  * Arguments: node
  * Returns a collection of edges connected to the given node
  * Include the weight of the connection in the returned collection
* size
  * Arguments: none
  * Returns the total number of nodes in the graph

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* add_node:
  * time `O(1)`
  * space `O(1)`

* add_edge:
  * time `O(n)`
  * space `O(n)`

* get_nodes:
  * time `O(n)`
  * space `O(n)`

* get_neighbors:
  * time `O(n)`
  * space `O(n)`

* size:
  * time `O(1)`
  * space `O(1)`

## API
<!-- Description of each method publicly available in your Graph -->
* `add node`: Add a node to the graph, Arguments: value , Returns: The added node
* `add edge`: Adds a new edge between two nodes in the graph If specified, assign a weight to the edge Both nodes should already be in the Graph ,Arguments: 2 nodes to be connected by the edge, weight (optional) , Returns: nothing
* `get nodes`: Returns all of the nodes in the graph as a collection (set, list, or similar)
* `get neighbors`: Returns a collection of edges connected to the given node , Include the weight of the connection in the returned collection
* `size`: Returns the total number of nodes in the graph
