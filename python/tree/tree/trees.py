from tree.queue import Queue

class Node:

    def __init__(self, value):

        self.value = value

        self.left = None

        self.right = None


##############################################################################################


class Binary_Tree:

    def __init__(self):

        self.root = None

    ###############################################

    def pre_order(self):
        """ root-left-right """

        try:

            self.values = []

            if self.root == None:

                return "Tree is Empty"

            def tree(node):

                self.values += [node.value]

                if node.left:

                    tree(node.left)

                if node.right:

                    tree(node.right)

                return self.values

            return tree(self.root)

        except:

            return "Error in Pre Order"

    ###############################################

    def in_order(self):
        """ left-node-right"""

        try:

            self.values = []

            if not self.root:

                return "Tree is Empty"

            def tree(node):

                if node.left:

                    tree(node.left)

                self.values += [node.value]

                if node.right:

                    tree(node.right)

                return self.values

            return tree(self.root)

        except:

            return "Error in In Order"

    ###############################################

    def post_order(self):
        """ left-right-node"""

        try:

            self.values = []

            if not self.root:

                return "Tree is Empty"

            def tree(node):

                if node.left:

                    tree(node.left)

                if node.right:

                    tree(node.right)

                self.values += [node.value]

                return self.values

            return tree(self.root)

        except:

            return "Error in Post Order"

  ###############################################

    def max(self):

        if not self.root:
            return "Tree is Empty"

        self.max = self.root.value

        def tree(node):
            if node.value > self.max:
                self.max = node.value
            if node.left:
                tree(node.left)
            if node.right:
                tree(node.right)
            return self.max

        return tree(self.root)

    ###############################################

    def breadth_first(tree):
        queue1=Queue()
        final_output = []

        if  tree.root:
                queue1.enqueue(tree.root)
        else:
            return "there is no root "

        while not queue1.is_empty():
            front=queue1.dequeue()
            final_output.append(front.value)

            if front.left :
                    queue1.enqueue(front.left)
            if front.right :
                    queue1.enqueue(front.right)
        return final_output

##############################################################################################


class Binary_Search_Tree(Binary_Tree):
    def add(self, value):
        '''add value to binery tree '''
        if self.root == None:
            self.root = Node(value)
        else:
            current = self.root
            while current:
                if value < current.value:
                    if current.left == None:
                        current.left = Node(value)
                        break
                    current = current.left
                else:
                    if current.right == None:
                        current.right = Node(value)
                        break
                    current = current.right

    ###############################################
    def Contains(self, value):
        if self.root == None:
            return 'Tree is Empty'
        else:
            current = self.root
            while current:
                if current.value == value:
                    return True
                elif value < current.value:
                    if current.left == None:
                        return False
                    current = current.left
                else:

                    if current.right == None:
                        return False
                    current = current.right


###############################################


if __name__ == '__main__':
    tree = Binary_Tree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.right.right = Node(9)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right.left = Node(4)
    print(tree.breadth_first())