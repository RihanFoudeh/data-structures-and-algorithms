from hashtable.hashmap_tree_intersection import tree_intersection
from hashtable.trees import Binary_Tree, Node


def test_tree_intersection():
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

    actual = tree_intersection(tree_one, tree_two)
    expected = [100, 160, 125, 175, 200, 350, 500]
    assert actual == expected

#########################################################################


def test_tree_intersection_trees_empty():
    tree_one = Binary_Tree()

    tree_two = Binary_Tree()

    tree_two.root = Node(42)

    tree_two.root.left = Node(100)
    tree_two.root.right = Node(600)

    actual = tree_intersection(tree_one, tree_two)
    expected = "One Of The Trees Is Empty"
    assert actual == expected

#########################################################################


def test_tree_no_intersection():
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

    tree_two.root.left = Node(101)
    tree_two.root.right = Node(600)

    tree_two.root.left.left = Node(15)
    tree_two.root.left.right = Node(161)

    tree_two.root.right.left = Node(201)
    tree_two.root.right.right = Node(351)

    tree_two.root.left.right.left = Node(126)
    tree_two.root.left.right.right = Node(176)

    tree_two.root.right.right.left = Node(4)
    tree_two.root.right.right.right = Node(501)

    actual = tree_intersection(tree_one, tree_two)
    expected = "No Intersection"
    assert actual == expected

#########################################################################
