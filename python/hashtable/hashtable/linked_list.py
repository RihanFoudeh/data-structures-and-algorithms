class Node:

    """
    Function to initialise the node Class
    """
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    """
    Creating Nodes in linked List way
    """
    # counter=0
    def __init__(self):
        self.head = None


    def append(self, valueAdded):
        """
        Method to add values to the end of nodes
        """
        # LinkedList.counter += 1
        node = Node(valueAdded)
        if self.head == None:
            self.head = node
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
            return "value added"




    def insert(self, valueAdded):
        """
        Method to add values at the beginning  nodes
        """
        node = Node(valueAdded)

        if self.head==None:
            self.head=node

        else:

            node.next=self.head

            self.head=node


        return "value added"

    def includes(self, valueSearched):
        """
        method to search for a specifc value
        """
        current = self.head
        if self.head!=None:
            while current.next != None:
                if current.value == valueSearched:
                    print ("true")
                    return True

                current = current.next
            print ("false")
            return False
        else:
            print ("Empty")
            return ("Empty")


    def __str__(self):
        if self.head :
            data_str=''
            current=self.head
            while current:
                data_str+='{'+str(current.value)+'}->'
                current=current.next
            data_str+='null'
            return data_str
