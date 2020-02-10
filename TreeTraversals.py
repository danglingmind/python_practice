class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, root_element: Node):
        self.root = root_element

    # depth first Traversal version
    def inorder_traversal(self):
        print('Inorder Traversal of the Tree')
        self.__intraversal(self.root)
        print(end='\n')

    def __intraversal(self, temproot):
        if temproot == None:
            return
        else:
            self.__intraversal(temproot.left)
            print(temproot.data, end=' ')
            self.__intraversal(temproot.right)

    # depth first Traversal version
    def preorder_traversal(self):
        print("Pre order Traversal of the Tree")
        self.__pretraversal(self.root)
        print(end='\n')

    def __pretraversal(self, temproot):
        if temproot == None:
            return
        else:
            print(temproot.data, end=' ')
            self.__pretraversal(temproot.left)
            self.__pretraversal(temproot.right)

    # depth first Traversal version
    def postorder_traversal(self):
        print("Post order Traversal of the Tree")
        self.__posttraversal(self.root)
        print(end='\n')

    def __posttraversal(self, temproot):
        if temproot == None:
            return
        else:
            self.__posttraversal(temproot.left)
            self.__posttraversal(temproot.right)
            print(temproot.data, end=' ')

    # Breadth first traversal(level order traversal)
    def breadthFirst_traversal(self):
        print('Breadth First Traversal of the Tree')
        self.__bfs(self.root)
        print(end='\n')

    def __bfs(self,temproot):
        if temproot == None:
            return
        else:
            # list for traversal
            q = [temproot]
            # insert root in the beginning
            while len(q) > 0:
                cur = q.pop(0)
                print(cur.data,end=' ')
                if cur.left != None:
                    q.append(cur.left)
                if cur.right != None:
                    q.append(cur.right)
        print(end='\n')




if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)

    T = Tree(root)
    T.inorder_traversal()
    T.preorder_traversal()
    T.postorder_traversal()
    T.breadthFirst_traversal()
