class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root: Node):
        self.root = root

    def InorderTraverse_iterative(self):
        print("Iterative Inorder Traversal")
        self.__intraverse(self.root)

    def __intraverse(self, temproot: Node):
        if temproot == None:
            return
        else:
            # create a stack for storing traversed nodes
            s = []

            while len(s) > 0 or temproot != None:
                if temproot != None:
                    s.append(temproot)
                    temproot = temproot.left
                else:
                    temproot = s.pop(len(s) - 1)
                    print(temproot.data, end=' ')
                    temproot = temproot.right

    def PreorderIterative(self):
        print('Preorder iterative ')
        self.__preordertraverse(self.root)
        print(end=' ')

    def __preordertraverse(self, temproot: Node):
        s = []
        while len(s) > 0 or temproot != None:
            if temproot != None:
                print(temproot.data, end=' ')
                s.append(temproot.left)
                temproot = temproot.left
            else:
                t = s.pop(len(s) - 1)
                if t != None:
                    temproot = t
                    temproot = temproot.right


if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    T = Tree(root)
    T.InorderTraverse_iterative()
    T.PreorderIterative()
