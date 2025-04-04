class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked:
    def __init__(self):
        self.head = None

    def insertAtbeginning(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode

    def insertInbetween(self, value, k):
        newnode = Node(value)
        temp = self.head
        while temp and temp.data != k:
            temp = temp.next

        if temp is None:
            print("There is no such node ")
            return

        newnode.next = temp.next
        temp.next = newnode

    def deleteNode(self, k):
        temp = self.head
        prev = temp

        if self.head is None:
            print("LL is empty!!")
            return

        if self.head.data == k:
            self.head = self.head.next
            return

        while temp and temp.data != k:
            prev = temp
            temp = temp.next

        prev.next = temp.next

    def rotateLinked(self, k):
        # Handle edge cases
        if not self.head or not self.head.next or k <= 0:
            return self.head

        # Find length and link tail to head to make a circular list
        length = 1
        tail = self.head
        while tail.next:
            tail = tail.next
            length += 1

        # Optimize k if larger than length
        k = k % length
        if k == 0:
            return self.head

        # Make the list circular
        tail.next = self.head

        # Find the new tail and head positions
        current = self.head
        for _ in range(k - 1):
            current = current.next

        # Break the circular link
        self.head = current.next
        current.next = None

        return self.head

    def printLinked(self):
        temp = self.head
        while temp:
            print(temp.data, "->", end=" ")
            temp = temp.next

        print("NULL")


if __name__ == "__main__":
    ll = Linked()
    ll.insertAtbeginning(50)
    ll.insertAtbeginning(40)
    ll.insertAtbeginning(30)
    ll.insertAtbeginning(20)
    ll.insertAtbeginning(10)

    ll.printLinked()
    k = int(input())
    ll.rotateLinked(k)
    ll.printLinked()
