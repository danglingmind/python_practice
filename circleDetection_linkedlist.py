# node class
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None

if __name__ == '__main__':
    h = LinkedList()

    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)

    h.head = n1
    h.head.next = n2
    h.head.next.next = n3
    h.head.next.next.next = n4
    h.head.next.next.next.next = n5
    h.head.next.next.next.next.next = n6

    # make a cycle
    n6.next = n4

    # # print the list
    # t = h.head
    # while t != None:
    #     print(t.data)
    #     t = t.next


    # detect the cycle in the list

    if h.head == None:
        print('list is empty')
        exit()

    if h.head.next == None:
        print('only one node is in the list')
        exit()

    #  find the cycle
    fast = h.head
    slow = h.head


    while fast and slow and fast.next :
        slow = slow.next
        fast = fast.next.next

        if slow == fast :
            print('here it is')
            break
            exit()