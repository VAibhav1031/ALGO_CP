class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Linked:
    def list_to_linked(self, values):
        if not values:
            return None

        head = ListNode(values[0])
        current = head
        for value in values[1:]:
            current.next = ListNode(value)
            current = current.next

        return head


class Solution:
    def addTwoNumbers(self, l1, l2):
        k = Linked()
        l1_head = k.list_to_linked(l1)
        l2_head = k.list_to_linked(l2)

        carry = 0
        dummy = ListNode(0)
        current = dummy

        while l1_head or l2_head or carry:
            val1 = l1_head.val if l1_head else 0
            val2 = l2_head.val if l2_head else 0

            sum_ = val1 + val2 + carry
            carry = sum_ // 10
            current.next = ListNode(sum_ % 10)

            current = current.next

            if l1_head:
                l1_head = l1_head.next
            if l2_head:
                l2_head = l2_head.next

        return dummy.next


if __name__ == "__main__":
    # Input
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))

    sol = Solution()
    result = sol.addTwoNumbers(l1, l2)

    # Convert result linked list back to a list for display
    def linked_to_list(head):
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    print(linked_to_list(result))  # Output: [7, 0, 8]
