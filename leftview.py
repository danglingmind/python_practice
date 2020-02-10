class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def leftview(root):
    # max_level=0
    max_level=[0]
    printleftview(root, max_level, 1)
def printleftview(root:Node, max_level, current_level):
    if root == None:
        return

    if current_level > max_level[0]:
        print(root.data, end=' ')
        max_level[0] = current_level

    printleftview(root.left, max_level, current_level+1)
    printleftview(root.right, max_level, current_level+1)

def rightview(root):
    max_level=[0]
    printrightview(root, max_level, 1)
def printrightview(root, max_level, current_level):
    if root==None:
        return

    if current_level > max_level[0]:
        print(root.data, end=' ')
        max_level[0]=current_level

    printrightview(root.right, max_level, current_level+1)
    printrightview(root.left, max_level, current_level+1)

def commonancestor(root, node1, node2):
    if root == None:
        return None

    if root.data == node1 or root.data == node2:
        return root

    l = commonancestor(root.left, node1, node2)
    r = commonancestor(root.right, node1, node2)

    if l and r :
        return root
    return l if l is not None else r

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.right = Node(6)
    root.right.left = Node(7)

    leftview(root)

    print(end='\n')
    rightview(root)

    print(commonancestor(root,4, 6).data)