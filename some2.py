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

    def swap_node(self, head):
        if not head or not head.next:
            return head

        dummy = ListtNode(0)
        dummy.next = head

        prev = dummy
        while head and head.next:
            first = head
            second = head.next

            # swap
            prev.next = second
            first.next = second.next
            second.next = first

            # moving the prev to first
            prev = first
            head = head.next  # this plays more  imprtant time
            # of moving the thing

        return dummy.next

    def print_l(self, p):
        if not p:
            return "Empty BABY!!!"

        temp = p

        while temp:
            print(temp.value, " -> ", end="")
            temp = temp.next

        print("Null")


if __name__ == "__main__":
    n = list(map(int, input().split()))
    ll = LinkedList()
    s = ll.list_to_Ll(n)

    ll.print_l(s)

    m = ll.swap_node(s)

    ll.print_l(m)
