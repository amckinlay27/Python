#Adam McKinlay - c0656685
#Date: 2019-12-03
#Double Linked List Assign

#Node
class Node():
    #Init
    def __init__(self, data=0):
        self.data = data
        self.next = None
        self.prev = None

    #To string
    def __str__(self):
        return str(self.data)

#DoubleLinkedList
class DoubleLinkedList():
    #Init
    def __init__(self, head=None):
        self.head = head

    #To string
    def __str__(self):
        output = ""
        temp = self.head
        while(temp != None):
            output += str(temp.data) + " "
            temp = temp.next
        return output

    #Inserts node at beginning of list
    def insert_beg(self, newNode):
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head    #save list to temp
            self.head = newNode #point list to new node
            temp.prev = newNode #point prev of temp to new node
            newNode.next = temp #Join new node to temp

    #Inserts node at end of list
    def insert_end(self, newNode):
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            while(temp.next != None):#Search till end
                temp = temp.next
            temp.next = newNode      #original list point next to new node
            newNode.prev = temp      #Prev link new node to list

    #Inserts node after pos in list
    def insert_after(self, pos, newNode):
        if(self.head == None):
            self.head = newNode
            return
        else:
            temp = self.head
            for i in range(1,pos):        #-> until pos found
                temp = temp.next          
            newNode.next = temp.next      
            temp.next.previous = newNode  #Skip over to insert at pos
            temp.next = newNode    
            newNode.prev = temp

    #Deletes node from list after position
    def del_at(self, pos):
        s = self.head
        for i in range(1, pos): #find pos
            s = s.next
        remove = s.next         #node to remove
        s.next = remove.next    #skip over remove
        remove.next.prev = s    #skip over and point back early list 
        del remove

#Main Function
def main():
    #Declare and Init Nodes
    node1 = Node(10)
    node2 = Node(20)
    node3 = Node(30)
    node4 = Node(1)
    node5 = Node(8)
    node6 = Node(12)
    node7 = Node(54)

    #Declare and Init DoubleLinkedList
    lst = DoubleLinkedList()

    #insert_beg and Check
    lst.insert_beg(node1)
    lst.insert_beg(node2)
    lst.insert_beg(node3)
    print(lst)

    #insert_end and Check
    lst.insert_end(node4)
    lst.insert_end(node5)
    print(lst)

    #insert_after and Check
    lst.insert_after(2, node6)
    print(lst)
    lst.insert_after(5, node7)
    print(lst)

    #del_at and Check
    lst.del_at(2)
    print(lst)
    lst.del_at(4)
    print(lst)

#Call Main
main()










            
        
