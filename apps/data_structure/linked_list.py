from typing import Optional

class Node():
    def __init__(self, data, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev

class SLinkedList():
    def __init__(self) -> None:
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

    def prepend(self, value):
        newNode = Node(value, next=self.head)

        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head = newNode

    def append(self, value):
        newNode = Node(value, next=None)

        if self.tail is None:
            self.tail = newNode
            self.head = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def add_after(self, value, after):
        currentNode = self.head
        newNode = Node(value, next=None)
        nextNode = None

        while currentNode is not None:
            if currentNode.data == after:
                nextNode = currentNode.next
                currentNode.next = newNode
                newNode.next = nextNode
                return

            currentNode = currentNode.next

        print(f"[{after}] tidak ada dalam linked list!")

    def add_before(self, value, before):
        currentNode = self.head
        nextNode = None if currentNode is None else currentNode.next
        newNode = Node(value)

        while currentNode is not None:
            if nextNode is not None and nextNode.data == before:
                currentNode.next = newNode
                newNode.next = nextNode
                return

        print(f"[{before}] tidak ada dalam linked list!")

    def traverse(self):
        currentNode = self.head
        string_result = ""

        if currentNode == None:
            print("None")
        else:
            while currentNode is not None:
                string_result += f"[{currentNode.data}] -> "
                currentNode = currentNode.next

            print(string_result + "None")

    def display(self):
        currentNode = self.head

        if currentNode == None:
            return None
        else:
            while currentNode is not None:
                yield currentNode.data
                currentNode = currentNode.next


    def contain(self, value):
        currentNode = self.head
        
        while currentNode is not None:
            if currentNode.data == value:
                return True

            currentNode = currentNode.next

        return False

    def getFirst(self):
        return None if self.head is None else self.head.data

    def getLast(self):
        return None if self.tail is None else self.tail.data

    def popLeft(self):
        firstNode = self.head

        if firstNode is None:
            return None
        else:
            self.head = firstNode.next
            return firstNode.data

    def pop(self):
        currentNode = self.head
        nextNode = None if currentNode is None else currentNode.next

        if currentNode is None:
            return None
        elif currentNode.next is None:
            self.head = None
            self.tail = None
            return currentNode.data
        else:
            while currentNode is not None:
                if nextNode is not None and nextNode.next is None:
                    currentNode.next = None
                    self.tail = currentNode
                    return nextNode.data

                currentNode = currentNode.next
                nextNode = None if currentNode is None else currentNode.next

    def remove(self, value):
        currentNode = self.head
        nextNode = None if currentNode is None else currentNode.next

        if currentNode is None:
            print("Linked list kosong!")
        elif currentNode.next is None:
            if currentNode.data == value:
                self.head = None
                self.tail = None
            else:
                print(f"[{value}] tidak ada dalam linked list!")
        else:
            while currentNode is not None:
                if currentNode.data == value:
                    self.head = currentNode.next
                    return
                elif nextNode is not None and nextNode.data == value:
                    currentNode.next = nextNode.next
                    return

                currentNode = currentNode.next
                nextNode = None if currentNode is None else currentNode.next

            print(f"[{value}] tidak ada dalam linked list!")

    def empty(self):
        return True if self.head is None else False
