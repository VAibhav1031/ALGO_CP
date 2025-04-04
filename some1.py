# class Heap:
#     def __init
#
#
#
#

import heapq


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

    def mergeKList(self, k_list):
        if not k_list:
            return

        dummy = ListtNode(0)
        current = dummy

        heap = []
        for i, v in enumerate(k_list):
            heapq.heappush(heap, (v.value, id(v), v))

        while heap:
            _, _, node = heapq.heappop(heap)

            current.next = node
            current = current.next

            if node.next:
                heapq.heappush(heap, (node.next.value, id(node), node.next))

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
    #  we can  make different way od
    n = list(map(int, input().split()))
    n1 = list(map(int, input().split()))
    n2 = list(map(int, input().split()))

    ll = LinkedList()

    k = ll.list_to_Ll(n)
    k1 = ll.list_to_Ll(n1)
    k2 = ll.list_to_Ll(n2)
    k = list((k, k1, k2))

    # ll.print_l(k)

    m = ll.mergeKList(k)

    ll.print_l(m)
