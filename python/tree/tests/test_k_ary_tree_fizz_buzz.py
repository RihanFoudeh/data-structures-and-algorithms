from tree.k_ary_tree import K_ary_tree_fizz_buzz, K_ary_tree, Node

####################################################################

def test_K_ary_tree_fizz_buzz_empty():

    k_ary_tree = K_ary_tree()

    actual = K_ary_tree_fizz_buzz(k_ary_tree)

    expected = "K-ary tree is Empty"

    assert actual == expected

####################################################################

def test_K_ary_tree_fizz_buzz():

    k_ary_tree = K_ary_tree()
    k_ary_tree.root = Node(2)
    k_ary_tree.root.children += [Node(7)]
    k_ary_tree.root.children += [Node(5)]
    k_ary_tree.root.children += [Node(2)]
    k_ary_tree.root.children += [Node(6)]
    k_ary_tree.root.children += [Node(9)]
    k_ary_tree.root.children += [Node(5)]
    k_ary_tree.root.children += [Node(11)]
    k_ary_tree.root.children += [Node(15)]

    actual = K_ary_tree_fizz_buzz(k_ary_tree).__str__()

    expected = "['2', '7', 'Buzz', '2', 'Fizz', 'Fizz', 'Buzz', '11', 'FizzBuzz']"

    assert expected == actual

####################################################################
