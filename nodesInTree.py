class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self, root: Node):
        self.root = root

    def NodeCount(self):
        print('Total Node in Tree: ', end=' ')
        print(self.__countNodes(self.root))
    def __countNodes(self,temproot):
        if temproot == None:
            return 0
        else:
            return 1 + self.__countNodes(temproot.left) + self.__countNodes(temproot.right)


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    t = Tree(root)
    t.NodeCount()