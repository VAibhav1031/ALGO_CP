# Merge two list
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

    def print_l(self, p):
        if not p:
            return "Empty BABY!!!"

        temp = p

        while temp:
            print(temp.value, " -> ", end="")
            temp = temp.next

        print("Null")

    def mergeTwoLists(self, list1, list2):
        if not list1:
            return list2

        if not list2:
            return list1

        l1 = list1
        l2 = list2

        dummy = ListtNode(0)
        current = dummy
        while l1 and l2:
            if l1.value < l2.value:
                current.next = ListtNode(l1.value)
                l1 = l1.next

            else:
                current.next = ListtNode(l2.value)
                l2 = l2.next

            current = current.next

        if l1:
            current.next = l1

        if l2:
            current.next = l2

        return dummy.next


if __name__ == "__main__":
    n = list(map(int, input().split()))
    n1 = list(map(int, input().split()))

    ll = LinkedList()
    k = ll.list_to_Ll(n)
    k1 = ll.list_to_Ll(n1)

    ll.print_l(k)
    ll.print_l(k1)

    print()
    m = ll.mergeTwoLists(k, k1)

    ll.print_l(m)
