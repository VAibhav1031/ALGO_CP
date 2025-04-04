from typing import List


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

    def reverse(self, head):
        if not head:
            return None

        prev = None
        current = head

        while current:
            next_node = current.next
            # capturing the  next node   which will gonna  point to current one
            current.next = prev  # Pointing the  current node to the previous node
            prev = current  # moving the previous to current
            current = next_node  # moving current pointer to the next node

            # continueing the same prcedure to next_node until we got out out bound
            # This will let ust to reverse side by side

        return prev

    def reverseKGroup(self, head, k):
        # we have  to reverse in the LinkedList every k
        # we can implement reverse on  small // K chunks
        # aim  is  to move  the window like  thing where if the current window have k element the reverse it

        def reverse(head, k):
            current = head
            prev = None

            while k > 0:
                next_node = current.next  # storing the  next node
                current.next = prev  # current node pointing to the prev node
                prev = current  # moving prev to current
                current = next_node  # moving current to next node
                k -= 1

                return prev

        current = head
        length = 0
        while current:
            length += 1  # calculating the lenght of the linked lists
            current = current.next

        dummy = ListtNode(0)
        dummy.next = head  # this help in creating new way of linked list
        current = head
        prev_tail = (
            dummy  # plays important role in connecting the reversed linked lists groups
        )

        # will only work if lenght is greater than k (required on)
        while length >= k:
            start = current  # new  start for every group

            for _ in range(k):
                current = current.next  # moving the current to new current

            # will reverse from start upto k length
            new_head = reverse(start, k)
            prev_tail.next = (
                new_head  # main crux where we connect previous group to new group
            )
            prev_tail = start  # shift our prev_tail pointer to new start

            length -= k  # changing the length after k length group revers

        prev_tail.next = current  # if any left node which cant able to make to k group

        return dummy.next  # returning the head


if __name__ == "__main__":
    n = list(map(int, input().split()))
    m = int(input())
    ll = LinkedList()
    k = ll.list_to_Ll(n)
    ll.print_l(k)
    m = ll.reverseKGroup(k, m)
    ll.print_l(m)
