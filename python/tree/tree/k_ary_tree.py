from tree.queue import Queue

import copy

####################################################################

class Node:
    def __init__( self, value ):
        self.value = value
        self.children = []

####################################################################

class K_ary_tree:
    def __init__( self ):
        self.root = None

    def __str__( self ):

        if self.root:

            result = [self.root.value]

            for child in self.root.children:
                result += [child.value]

            result = str(result)

            return result

        else:
            return  "K-ary tree is Empty"

####################################################################

def K_ary_tree_fizz_buzz( k_ary_tree ):

    new_k_ary_tree = copy.deepcopy(k_ary_tree)

    root = new_k_ary_tree.root
    queue_nodes = Queue()

    if not root :
        return "K-ary tree is Empty"

    def check_fizz_buzz(node):
        if node % 3 == 0 and node % 5 == 0:
            return ('FizzBuzz')
        elif node % 3 == 0:
            return ('Fizz')
        elif node % 5 == 0:
            return ('Buzz')
        else:
            return str(node)

    if root :
        queue_nodes.enqueue( root )

    while not queue_nodes.isEmpty():

        nodes = queue_nodes.dequeue()

        nodes.value = check_fizz_buzz(nodes.value)

        for child in nodes.children:
            queue_nodes.enqueue( child )

    return new_k_ary_tree

####################################################################
####################################################################

if __name__=='__main__':
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


    print(f"Old k ary tree : {k_ary_tree}")

    new_k_ary_tree = K_ary_tree_fizz_buzz( k_ary_tree )
    print(f"New k ary tree Fizz Buzz : {new_k_ary_tree}")

    print(f"Old k ary tree : {k_ary_tree}")
####################################################################
####################################################################
