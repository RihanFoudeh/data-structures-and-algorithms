# Trees

# PR Description Section :

| Table Of Content                               | Links                                       |
| ---------------------------------------------- | ------------------------------------------- |
| PR '1' > Trees                                 | [PR '1' > Trees](https://github.com/RihanFoudeh/data-structures-and-algorithms/pull/22)|

<!-- Short summary or background information -->
## Trees Summary

### Trees Data Structure represent nodes connected by edges.

## Challenge
<!-- Description of the challenge -->

### Features

#### Node

* Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

#### Binary Tree

* Create a Binary Tree class
  * Define a method for each of the depth first traversals:
    * pre order
    * in order
    * post order which returns an array of the values, ordered appropriately.
  * Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab.

#### Binary Search Tree

* Create a Binary Search Tree class
  * This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
  * Add
    * Arguments: value
    * Return: nothing
    * Adds a new node with that value in the correct location in the binary search tree.
* Contains
  * Argument: value
  * Returns: boolean indicating whether or not the value is in the tree at least once.

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* pre order: time `O(n)`, space `O(n)`
* in order: time `O(n)`, space `O(n)`
* post order: time `O(n)`, space `O(n)`
* Add: time `O(logn)`, space `O(1)`
* Contains: time `O(logn)`, space `O(1)`

## API
<!-- Description of each method publicly available in each of your trees -->
* Pre order: method that return tree in order `< root=> left=> right >`
* In order: method that return tree in order `< left=> root=> right >`
* Post order: method that return tree in order `< left=> right=> root >`
* Add: to add a value to a tree by binary search algorithm
* Contains: to check if the tree contains a value

