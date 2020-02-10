class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
class Tree:
    def __init__(self, root: Node):
        self.root = root

    def vertical_traversal(self):
        temproot = self.root
        if temproot == None:
            return

        m = {}

        q = [(temproot, 0)]

        while len(q) > 0:
            t = q.pop(0)
            nd, d = t
            if m.get(d)==None:
                m[d] = []
            m[d].append(nd.data)
            if nd.left != None:
                q.append((nd.left, d-1))
            if nd.right != None:
                q.append((nd.right, d+1))

        for i in sorted(m.keys()):
            print((i, m[i][0]))   # prints top view of the tree



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.right.left = Node(7)

    t= Tree(root)
    t.vertical_traversal()