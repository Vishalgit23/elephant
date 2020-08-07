# // single linked list
class LinkedList:
    def __init__(self):
        self.head = None
        
    def printlinkedlist(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

    
linkedlistobj = LinkedList()  

firstnode = Node(10)
secondnode = Node(20)
thirdnode = Node(30)
fourthnode = Node(40)


linkedlistobj.head = firstnode
firstnode.next = secondnode
secondnode.next = thirdnode
thirdnode.next = fourthnode

linkedlistobj.printlinkedlist()



