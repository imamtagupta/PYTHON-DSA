class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        

class LinkedList:
    def __init__(self):
        self.head = None
    def appendLast(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            currentNode = self.head
            while currentNode.next is not None:
                currentNode = currentNode.next
            currentNode.next = Node(value)
            
    def appendFirst(self, value):
        if self.head is None:
            self.head = Node(value)
        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp
            
    def append(self, value, index):
        if index < 0 and index > self.length():
            return
        if self.head is None:
            self.appendFirst(value)
        else:
            prev, curr = None, self.head
            newNode = Node(value)
            for i in range(index):
                prev = curr
                curr = curr.next
            if prev is None:
                head = newNode
            else:
                prev.next = newNode
            newNode.next = curr
            
            
    def removeFirst(self):
        if self.head is None:
            return
        self.head = self.head.next
        
    def removeLast(self):
        if self.head is None:
            return
        if self.length() < 2:
            return self.removeFirst()
        current = self.head
        while current.next.next is not None:
            current = current.next
        current.next = None
        
    def remove(self,index):
        ln = length(head)
        if (pos < 0) or (pos >= ln) or (head == None):
            return head
        prev, temp = None, head
        while pos > 0:
            prev = temp
            temp = temp.next
            pos -= 1
        if prev is None:
            head = head.next
        else:
            prev.next = temp.next
        return head
        
    def show(self):
        currentNode = self.head
        while currentNode is not None:
            print(f'{currentNode.data} -> ', end="")
            currentNode = currentNode.next
        print('None')
        
    def length(self):
        count = 0
        currentNode = self.head
        while currentNode is not None:
            currentNode = currentNode.next
            count += 1
        return count
    
    def get(self, index):
        i = 0
        currentNode = self.head
        while currentNode is not None:
            if i == index:
                return currentNode.data
            currentNode = currentNode.next
            i += 1
        return None
        
        