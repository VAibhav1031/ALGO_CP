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
        if not self.head or k <= 0:
            return
        length = 1
        tail = self.head
        while tail.next:
            tail = tail.next
            length += 1

        for _ in range(k):
            t = self.head
            self.head = self.head.next
            tail.next = t
            t.next = None
            tail = tail.next
            # print(tail.data)

    def printLinked(self):
        temp = self.head
        while temp:
            print(temp.data, "->", end=" ")
            temp = temp.next

        print("NULL")


if __name__ == "__main__":
    # # Test 1: Empty list operations
    # print("Test case : 1\n")
    # ll = Linked()
    # print("Printing empty list:")
    # ll.printLinked()  # Expected: "NULL"
    # print()
    #
    # print("Test case :2\n")
    # # Test 2: Insert at the beginning
    # ll.insertAtbeginning(10)
    # ll.insertAtbeginning(20)
    # ll.insertAtbeginning(30)
    # print("List after inserting 30, 20, 10 at the beginning:")
    # ll.printLinked()  # Expected: "30 -> 20 -> 10 -> NULL"
    # print()
    #
    # print("Test Case : 3\n")
    # # Test 3: Insert in between (valid case)
    # ll.insertInbetween(25, 20)
    # print("List after inserting 25 after 20:")
    # ll.printLinked()  # Expected: "30 -> 20 -> 25 -> 10 -> NULL"
    #
    # print()
    #
    # print("Test Case : 4\n")
    # # Test 4: Insert in between (node not found)
    # ll.insertInbetween(40, 50)  # Node with value 50 does not exist
    # # Expected output: "There is no such node."
    #
    # print()
    #
    # print("Test Case : 5\n")
    # # Test 5: Insert after the last node
    # ll.insertInbetween(5, 10)
    # print("List after inserting 5 after 10:")
    # ll.printLinked()  # Expected: "30 -> 20 -> 25 -> 10 -> 5 -> NULL"
    # print()
    #
    # print("Test case : 6\n")
    # # Test 6: Single node list
    # ll_single = Linked()
    # ll_single.insertAtbeginning(50)
    # print("Single node list:")
    # ll_single.printLinked()  # Expected: "50 -> NULL"
    #
    # # Insert after the only node
    # ll_single.insertInbetween(60, 50)
    # print("After inserting 60 after 50 in single node list:")
    # ll_single.printLinked()  # Expected: "50 -> 60 -> NULL"
    # print()
    #
    # print("Test case : 7\n")
    # # Test 7: Insert None value
    # ll.insertAtbeginning(None)
    # print("List after inserting None:")
    # ll.printLinked()  # Expected: "None -> 30 -> 20 -> 25 -> 10 -> 5 -> NULL"
    #
    # print()
    # print("Test Case: 8\n")
    # ll_1 = Linked()
    # ll_1.insertAtbeginning(10)
    # ll_1.insertAtbeginning(13)
    # ll_1.insertInbetween(2, 13)
    # ll_1.insertInbetween(6, 2)
    # ll_1.printLinked()
    # ll_1.deleteNode(10)
    # ll_1.printLinked()
    # ll_1.deleteNode(13)
    # ll_1.printLinked()

    ll = Linked()
    # ll.insertAtbeginning(50)
    ll.insertAtbeginning(40)
    ll.insertAtbeginning(30)
    ll.insertAtbeginning(20)
    ll.insertAtbeginning(10)

    ll.printLinked()
    k = int(input())
    ll.rotateLinked(k)
    ll.printLinked()
