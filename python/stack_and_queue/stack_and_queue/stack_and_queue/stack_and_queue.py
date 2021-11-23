class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
####################################################################
class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        node = Node(value)
        if self.top:
            node.next = self.top
        self.top = node
    def pop(self):

        if self.is_empty():
            raise Exception("This stack is empty")
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp.value

    def peek(self):


        if self.is_empty():
            raise Exception("This stack is empty")
        return self.top.value
    def is_empty(self):
        return self.top == None


####################################################################

class Queue():
    def __init__(self):
        self.front=None
        self.rear=None
    def enqueue(self , value):
        node=Node(value)
        if self.front ==None:
            self.front=node
            self.rear=node
        else:
            self.rear.next=node
            self.rear=node

    def dequeue(self):
        try:
            self.front.value
        except:
            return "This is Empty queue"
        else:
            temp=self.front
            self.front=temp.next
            temp.next=None
            return temp.value
    def peek(self):
        try:
            return self.front.value
        except:
            return "This is Empty queue"
    def isEmpty (self):
        if self.front == None and self.rear == None :
            return True
        else:
            return False

    def __str__(self):
        content=''
        current = self.rear
        content+="Null"
        while current:
            content+= f"-> {{{str(current.value)}}}"
            current=current.next
        return content

####################################################################

if __name__=="__main__" :
    print("### Stack ###")
    stack1 = Stack()
    stack1.push(3)
    stack1.push(13)
    stack1.push(23)
    stack1.push(33)
    print(stack1.__str__())
