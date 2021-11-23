# Trees

# PR Description Section :

| Table Of Content                               | Links                                       |
| ---------------------------------------------- | ------------------------------------------- |
| PR '1' > Trees                                 | [PR '1' > Trees](https://github.com/RihanFoudeh/data-structures-and-algorithms/pull/22)|
| PR '2' > tree-max                                 | [PR '2' > tree-max](https://github.com/RihanFoudeh/data-structures-and-algorithms/pull/23)|
| PR '3' > tree-breadth-first                                 | [PR '3' > tree-breadth-first](https://github.com/RihanFoudeh/data-structures-and-algorithms/tree/tree-breadth-first/python/tree)|
| PR '4' > tree-fizz-buzz                                | [PR '4' > tree-fizz-buzz](https://github.com/RihanFoudeh/data-structures-and-algorithms/pull/25)|




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


# Challenge Summary : Code Challenge: Class 16 : Find the Maximum Value in a Binary Tree
<!-- Description of the challenge -->

### Feature Tasks

#### Write the following method for the Binary Tree class

* find maximum value
  * Arguments: none
  * Returns: number

#### Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![tree-max](https://user-images.githubusercontent.com/73611547/142763894-42026c8b-83d6-455e-970c-6be6b5b5973f.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* max: time `O(n)`, space `O(1)`

## API

* max: method that return max value in tree

# Challenge Summary : Code Challenge: Class 17 : Breadth-first Traversal.
<!-- Description of the challenge -->
### Feature Tasks

* Write a function called breadth first
* Arguments: tree
* Return: list of all values in the tree, in the order they were encountered

#### `NOTE: Traverse the input tree using a Breadth-first approach`

## Whiteboard Process
<!-- Embedded whiteboard image -->
![tree-breadth-first](https://user-images.githubusercontent.com/73611547/142897728-0fb0ca84-4c58-4245-b5e4-5dbab4f679dd.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* Time : `O(n)`
* Space: `O(n)`


# Challenge Summary :  Code Challenge: Class 18 : Fizz Buzz Tree
<!-- Description of the challenge -->
### Feature Tasks

* Write a function called fizz buzz tree
* Arguments: k-ary tree
* Return: new k-ary tree

#### Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:

* If the value is divisible by 3, replace the value with “Fizz”
* If the value is divisible by 5, replace the value with “Buzz”
* If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
* If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process
<!-- Embedded whiteboard image -->
![tree-fizz-buzz](https://user-images.githubusercontent.com/73611547/143091961-fafc41cb-343c-423a-bf1d-475b730d1107.jpg)

## Approach & Efficiency
<!-- What approach did you take? Why? What is the Big O space/time for this approach? -->
* Time : `O(n)`
* Space: `O(n)`
