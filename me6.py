class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Linked:
    def list_to_linked(self, values):
        if not values:
            return
        head = Node(values[0])
        current = head
        for v in values[1:]:
            current.next = Node(v)
            current = current.next

        return head

    def printLink(self, head):
        if not head:
            return

        while head:
            print(head.data, "->", end="")
            head = head.next

        print("NULL")


# WE WILL PROVIDE  THE  SORTED Linked LIST
def merge(A, B):
    if not A or not B:  # if it is empty
        return

    f_head = A
    s_head = B
    dummy = Node(0)
    current_ = dummy
    while f_head or s_head:
        if not f_head:
            current_.next = s_head
            break
        # elif s_head == None:
        elif not s_head:
            current_.next = f_head
            break

        elif f_head.data > s_head.data:
            current_.next = s_head
            s_head = s_head.next
        else:
            current_.next = f_head
            f_head = f_head.next

        current_ = current_.next
    return dummy.next


#  i think  we have  to  divide given  linked list
# def mergeSort(ll):
#     if not ll:
#         return
#     lo = 0
#     while ll:
#         ll = ll.next
#         lo += 1
#
#     left = Node(0)
#     right = Node(0)
#     dummy_1 = left
#     dummy_2 = right
#     i = 0
#     while ll:
#         if i <= (lo // 2):
#             dummy_1.next = ll
#             dummy_1 = dummy_1.next
#         else:
#             dummy_2.next = ll
#             dummy_2 = dummy_2.next
#
#         ll = ll.next
#     l_ = left.next
#     r_ = right.next
#
#     lu = mergeSort(l_)
#     ru = mergeSort(r_)
#     return merge(lu, ru)


def mergeSort(ll):
    # Base case: empty list or single node
    if not ll or not ll.next:
        return ll

    # Splitting the list into two halves
    slow, fast = ll, ll.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next

    # Divide the list into two halves
    mid = slow.next
    slow.next = None

    # Recursive sort on each half
    left = mergeSort(ll)
    right = mergeSort(mid)

    # Merge the sorted halves
    return merge(left, right)


if __name__ == "__main__":
    n = list(map(int, input().split()))
    n1 = list(map(int, input().split()))
    ll = Linked()
    n_ll = ll.list_to_linked(n)
    n1_ll = ll.list_to_linked(n1)
    ll.printLink(n_ll)
    ll.printLink(n1_ll)
    print()
    k = merge(n_ll, n1_ll)
    ll.printLink(k)
    print("Trying to mergeSort")
    lis = list(map(int, input("Enter : ").split()))
    lis_ = ll.list_to_linked(lis)
    h = mergeSort(lis_)
    ll.printLink(h)
