from tree import __version__
from tree.trees import Binary_Search_Tree , Node , Binary_Tree

def test_version():
    assert __version__ == '0.1.0'

#################################################################################

def test_instantiate_an_empty_tree():
    b_tree=Binary_Search_Tree()
    actual=b_tree.root
    expected=None
    assert actual==expected

#################################################################################

def  test_instantiate_tree_single_root_node():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=tree.root.value
    expected=5
    assert actual==expected

#################################################################################

def test_add_left_child_right_child_single_root():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=(tree.root.left.value,tree.root.right.value)
    expected=(3,8)
    assert actual==expected

#################################################################################

def test_collection_from_preorder_traversal():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=tree.pre_order()
    expected=[5,3,8]
    assert actual==expected

#################################################################################

def test_collection_from_inorder_traversal():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=tree.in_order()
    expected=[3,5,8]
    assert actual==expected

#################################################################################

def test_collection_from_postorder_traversal():
    tree=Binary_Search_Tree()
    tree.add(5)
    tree.add(3)
    tree.add(8)
    actual=tree.post_order()
    expected=[3,8,5]
    assert actual==expected

#################################################################################
#################################################################################

def test_max_val():
    tree=Binary_Search_Tree()
    tree.root=Node(2)
    tree.root.left=Node(7)
    tree.root.left.left=Node(2)
    tree.root.left.right=Node(6)
    tree.root.left.right.left=Node(5)
    tree.root.left.right.right=Node(11)

    tree.root.right=Node(5)
    tree.root.right.right=Node(9)
    tree.root.right.right.left=Node(4)

    actual=tree.max()
    expected=11
    assert actual==expected

#################################################################################
#################################################################################

def test_breadth_first():
    tree = Binary_Tree()
    tree.root=Node(2)

    tree.root.left=Node(7)
    tree.root.right=Node(5)

    tree.root.left.left=Node(2)
    tree.root.left.right=Node(6)

    tree.root.right.right=Node(9)

    tree.root.left.right.left=Node(5)
    tree.root.left.right.right=Node(11)


    tree.root.right.right.left=Node(4)

    actual = tree.breadth_first()
    expected = [2,7,5,2,6,9,5,11,4]

    assert actual == expected

#################################################################################
#################################################################################

def test_fizz_buzz_tree_empty():
    tree = Binary_Tree()

    actual = tree.fizz_buzz_tree()
    expected = "Tree is Empty"

    assert actual == expected

#################################################################################

def test_fizz_buzz_tree():
    tree = Binary_Tree()
    tree.root=Node(2)

    tree.root.left=Node(7)
    tree.root.right=Node(5)

    tree.root.left.left=Node(2)
    tree.root.left.right=Node(6)

    tree.root.right.right=Node(9)

    tree.root.left.right.left=Node(5)
    tree.root.left.right.right=Node(11)


    tree.root.right.right.left=Node(15)

    fizz_buzz = tree.fizz_buzz_tree()
    actual = fizz_buzz.breadth_first()
    expected = ['2', '7', 'Buzz', '2', 'Fizz', 'Fizz', 'Buzz', '11', 'FizzBuzz']

    assert actual == expected

#################################################################################
#################################################################################
