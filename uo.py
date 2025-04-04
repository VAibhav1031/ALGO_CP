class ListtNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def list_to_Ll(self, l_: list[int]):
        dummy = ListtNode(0)
        current = dummy
        for i in range(len(l_)):
            current.next = ListtNode(l_[i])
            current = current.next

        return dummy.next

    def printL(self, l_):
        if not l_:
            return "Empty LinkedList"
        temp = l_
        while temp:
            print(temp.value, "->", end="")
            temp = temp.next

        print("Null")

    def deleteNode(self, head, n: int):
        prev = head
        temp = head

        if head.next is n:
            head.next = None

        while temp and temp.value != n:
            prev = temp
            temp = temp.next

        prev.next = temp.next  # unlinked the  part

    def removenthnodefromEnd(self, head, n: int):
        if not head:  # empty list
            return

        d = head
        l_ = 0
        while d:
            l_ += 1
            d = d.next

        if l_ == n:
            head = head.next
            return

        fast = head
        slow = head
        for _ in range(n):
            if not fast:
                return
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

    def addTwoList(self, head, head1):
        """
        In this  we are doing very simple
        Adding the  two LinkedList  like
        we have  the  two list [3, 5, 2] [2, 6, 7]

        """

        l1_head = head
        l2_head = head1

        carry = 0
        dummy = ListtNode(0)
        current = dummy
        while l1_head or l2_head or carry:
            val1 = l1_head.value if l1_head else 0
            val2 = l2_head.value if l2_head else 0

            sum_ = val1 + val2 + carry
            carry = sum_ // 10
            current.next = ListtNode(sum_ % 10)

            current = current.next

            if l1_head:
                l1_head = l1_head.next

            if l2_head:
                l2_head = l2_head.next

        return dummy.next


if __name__ == "__main__":
    n = list(map(int, input().split()))
    ll = LinkedList()
    k = ll.list_to_Ll(n)
    ll.printL(k)

    # ll.deleteNode(k, 1)
    #

    ll.removenthnodefromEnd(k, 2)
    ll.printL(k)

    print()
    print("ADDD\n")

    n = list(map(int, input().split()))
    n1 = list(map(int, input().split()))

    p = ll.list_to_Ll(n)
    p1 = ll.list_to_Ll(n1)
    a = ll.addTwoList(p, p1)

    ll.printL(a)
