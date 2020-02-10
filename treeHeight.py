class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self, root: Node):
        self.root = root

    def height(self):
        current_h = 0
        current_h = self.__getHeight(self.root)
        return current_h
    def __getHeight(self, temproot:Node):
        if temproot == None:
            return 0
        else:
            return 1 + max(self.__getHeight(temproot.left), self.__getHeight(temproot.right))


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    t = Tree(root)
    print(t.height())