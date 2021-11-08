class Node:
    def __init__(self,value):
        self.value= value
        self.next= None
#########################################################################
class Linkedlist:
    def __init__(self):
        self.head = None
####################################

    def insert(self, value):

        if not self.head:
            new_node = Node(value)
            self.head = new_node


####################################

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)
####################################
    def includes(self,value):
        if self.head:
            current =self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            return False
        else:
            raise Exception("Sorry, this list is empty , so plz insert a value")
####################################
    def __str__(self):
        if self.head:
            data_str = ''
            current = self.head
            while current:
                data_str += '{'+str(current.value)+'}-> '
                current = current.next
            data_str += 'NULL'
            return data_str
        else:
            raise Exception("Sorry, this list is empty , so plz insert a value ")
#########################################################################
# if __name__ == "__main__":

#         List =Linkedlist()
#         List.insert(3)
#         List.insert(3)
#         List.append(7)
#         List.append(13)
#         List.append(23)
#         print(List)
