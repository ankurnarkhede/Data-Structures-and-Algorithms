
# Implementation of Singly Linked list in Python


# Node of a Singly Linked List
class Node:
    # constructor
    def __init__(self, data):
        self.data = data
        self.next = None


    def set_data(self, data):
        # method for setting the data field of the node
        self.data = data


    def get_data(self):
        # method for getting the data field of the node
        return self.data

    def set_next(self, next):
        # method for setting the next field of the node
        self.next = next

    def get_next(self):
        # method for getting the next field of the node
        return self.next

    def has_next(self):
        # returns boolean true if the node points to another node
        return self.next != None


# class for defining a Singly linked list
class SinglyLinkedList (object):
    # initializing a list
    def __init__(self):
        self.length = 0
        self.head = None

    def addNode(self, node):
        # method to add a node in the linked list
        if self.length == 0:
            self.addBeg (node)
        else:
            self.addLast (node)

    def addBeg(self, node):
        # method to add a node at the beginning of the list with a data
        newNode = node
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def addAfterValue(self, data, node):
        # method to add a node AFTERRR the node having the data=data. The data of the new node is value2
        newNode = node
        currentnode = self.head

        while currentnode.next != None or currentnode.data != data:
            if currentnode.data == data:
                newNode.next = currentnode.next
                currentnode.next = newNode
                self.length +=1
                return
            else:
                currentnode = currentnode.next

        print("The data provided is not present")

    def addAtPos(self, pos, node):
        # method to add a node at a particular position
        count = 0
        currentnode = self.head
        previousnode = self.head

        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.next = node
                    node.next = currentnode
                    self.length += 1
                    return

                else:
                    previousnode = currentnode
                    currentnode = currentnode.next

    def addLast(self, node):
        # method to add a node at the end of a list
        currentnode = self.head

        while currentnode.next != None:
            currentnode = currentnode.next

        newNode = node
        newNode.next = None
        currentnode.next = newNode
        self.length = self.length + 1

    def deleteBeg(self):
        # method to delete the first node of the linked list
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.next
            self.length -= 1

    def deleteLast(self):
        # method to delete the last node of the linked list
        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.head
            previousnode = self.head

            while currentnode.next != None:
                previousnode = currentnode
                currentnode = currentnode.next

            previousnode.next = None

            self.length -= 1

    def deleteValue(self, data):
        # method to delete a node after the node having the given data
        currentnode = self.head
        previousnode = self.head

        while currentnode.next != None or currentnode.data != data:
            if currentnode.data == data:
                previousnode.next = currentnode.next
                self.length -= 1
                return

            else:
                previousnode = currentnode
                currentnode = currentnode.next

        print("The data provided is not present")

    def deleteAtPos(self, pos):
        # method to delete a node at a particular position
        count = 0
        currentnode = self.head
        previousnode = self.head

        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        # to deletle the first position of the linkedlist
        elif pos == 1:
            self.deleteBeg ()
            self.length -= 1
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.next = currentnode.next
                    self.length -= 1
                    return
                else:
                    previousnode = currentnode
                    currentnode = currentnode.next

    def getLength(self):
        # returns the length of the list
        return self.length

    def getFirst(self):
        # returns the first element of the list
        if self.length == 0:
            print("The list is empty")
        else:
            return self.head.data

    def getLast(self):

        # returns the last element of the list
        if self.length == 0:
            print("The list is empty")
        else:
            currentnode = self.head

            while currentnode.next != None:
                currentnode = currentnode.next

            return currentnode.data

    def getAtPos(self, pos):
        # returns node at any position
        count = 0
        currentnode = self.head

        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    return currentnode.data
                else:
                    currentnode = currentnode.next

    def print_list(self):
        # method to print the whole list
        nodeList = []
        currentnode = self.head
        while currentnode != None:
            nodeList.append (currentnode.data)
            currentnode = currentnode.next

        print(nodeList)

# almost all frequently used methods added



node1 = Node (1)
node2 = Node (2)
node3 = Node (3)
node4 = Node (4)
node5 = Node (5)
ll = SinglyLinkedList ()
ll.addNode (node1)
ll.addNode (node2)
ll.addNode (node3)
ll.addNode (node4)
ll.addNode (node5)
ll.print_list ()