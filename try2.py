import json
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next



def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def prettyPrintLinkedList(node):
    while node and node.next:
        print(str(node.val) + "->", end='')
        node = node.next

    if node:
        print(node.val)
    else:
        print("Empty LinkedList")

def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            node = stringToListNode(line)
            prettyPrintLinkedList(node)
        except StopIteration:
            break


def main1():
    filename = "input.txt"

    try:
        with open("input.txt","r") as file:
            for line in file:
                line = line.strip()
                if line:
                    h = stringToListNode(line)
                    prettyPrintLinkedList(h)

    except FileNotFoundError:
        print(f"Error file: '{filename}' not found ")

if __name__ == '__main__':
    #main()
    main1()
