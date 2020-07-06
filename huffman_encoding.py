import heapq
import random
class Node:
    def __init__(self, char, freq):
        self.value = (char, freq)
        self.left = None
        self.right = None


class MyHeap:
    def __init__(self):
        self.__actual_item_list = {}
        self.heap = []

    def push(self,item: Node):
        self.__actual_item_list[item.value[0]] = item
        char = item.value[0]
        freq = item.value[1]
        heapq.heappush(self.heap, (freq, char))

    def pop(self):
        if len(self.heap) > 0:
            freq, char = heapq.heappop(self.heap)
            return self.__actual_item_list.pop(char)
        else:
            return None


def print_huffman_codes(root: Node, path: str):
    if root.left == None and root.right == None:
        print(f'code : {path} - char : {root.value[0]}')
    else:
        if root.left:
            print_huffman_codes(root.left, path+'0')
        if root.right:
            print_huffman_codes(root.right, path+'1')


def list_freq_node_list(text: str):
    s = text.strip()
    freq = {}
    for i in s:
        if i in freq:
            freq[i] = freq[i] + 1
        else:
            freq[i] = 1

    node_list =[]
    for key in freq:
        node_list.append(Node(key, freq[key]))

    return node_list


def huffman_encode(text: str):
    # node list
    n_list = list_freq_node_list(text)

    # create a heap with a tupple (freq, node)
    h = MyHeap()
    for n in n_list:
        h.push(n)

    # create huffman tree
    while len(h.heap) > 0:
        if len(h.heap) == 1:
            break
        
        s1 = h.pop()
        s2 = h.pop()

        # create a intermediate node and append it into tree
        temp = Node(str(random.randint(1,10000)), s1.value[1]+s2.value[1])
        temp.left = s1
        temp.right = s2
        
        # add temp to heap
        h.push(temp)

    # print the codes for each character
    root = h.pop()

    print_huffman_codes(root,'')


if __name__ == '__main__':
    text = input('Enter any text: ')
    huffman_encode(text)
