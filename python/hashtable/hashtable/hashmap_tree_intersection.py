from hashtable.hashtable import HashTable

from hashtable.trees import Binary_Tree, Node

#########################################################################
#########################################################################


def tree_intersection(tree_one, tree_two):
    """
    Write a function called tree intersection
    Arguments: two binary trees
    Return: array
    """
    if not tree_one.root or not tree_two.root:
        return "One Of The Trees Is Empty"

    tree_arr1 = tree_one.pre_order()
    tree_arr2 = tree_two.pre_order()

    intersection = []
    new_hashtable = HashTable()

    [new_hashtable.add(node, node) for node in tree_arr1]

    [intersection.append(element)
     for element in tree_arr2 if new_hashtable.contains(element)]

    if intersection == []:
        return "No Intersection"

    return intersection


#########################################################################
#########################################################################
if __name__ == '__main__':

    tree_one = Binary_Tree()

    tree_one.root = Node(150)

    tree_one.root.left = Node(100)
    tree_one.root.right = Node(250)

    tree_one.root.left.left = Node(75)
    tree_one.root.left.right = Node(160)

    tree_one.root.right.left = Node(200)
    tree_one.root.right.right = Node(350)

    tree_one.root.left.right.left = Node(125)
    tree_one.root.left.right.right = Node(175)

    tree_one.root.right.right.left = Node(300)
    tree_one.root.right.right.right = Node(500)

    tree_two = Binary_Tree()

    tree_two.root = Node(42)

    tree_two.root.left = Node(100)
    tree_two.root.right = Node(600)

    tree_two.root.left.left = Node(15)
    tree_two.root.left.right = Node(160)

    tree_two.root.right.left = Node(200)
    tree_two.root.right.right = Node(350)

    tree_two.root.left.right.left = Node(125)
    tree_two.root.left.right.right = Node(175)

    tree_two.root.right.right.left = Node(4)
    tree_two.root.right.right.right = Node(500)

    intersection = tree_intersection(tree_one, tree_two)
    print(intersection)

#########################################################################
