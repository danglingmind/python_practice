# node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


if __name__ == '__main__':

    l1 = LinkedList()

    l1.head = Node(1)
    second = Node(2)
    third = Node(3)

    l1.head.next = second
    second.next = third

    # print list
    temp = l1.head

    while temp:
        print(temp.data)
        temp = temp.next
