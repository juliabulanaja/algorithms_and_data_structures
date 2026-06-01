import sys
import threading

sys.setrecursionlimit(10**6)
threading.stack_size(2**27)


class Tree:
    def __init__(self, vertices):
        self.key = list(map(lambda x: x[0], vertices))
        self.left = list(map(lambda x: x[1], vertices))
        self.right = list(map(lambda x: x[2], vertices))


    def in_order_traversal(self, i=0, result=[]):

        if not len(self.key) or i == -1:
            return result

        self.in_order_traversal(self.left[i], result)
        result.append(self.key[i])
        self.in_order_traversal(self.right[i], result)


    def pre_order_traversal(self, i=0, result=[]):
        if not len(self.key) or i == -1:
            return []
        
        result.append(self.key[i])
        self.pre_order_traversal(self.left[i], result) 
        self.pre_order_traversal(self.right[i], result)

        
    def post_order_traversal(self, i=0, result=[]):
        if not len(self.key) or i == -1:
            return []

        self.post_order_traversal(self.left[i], result)
        self.post_order_traversal(self.right[i], result) 
        result.append(self.key[i])

def main():

    n = int(input())
    vertices = []
    for _ in range(n):
        vertex = list(map(int, input().split(' ')))
        vertices.append(vertex)
    tree = Tree(vertices)


    result_in_order = []
    tree.in_order_traversal(0, result_in_order)
    print(' '.join(map(str, result_in_order)))

    result_pre_order = []
    tree.pre_order_traversal(0, result_pre_order)
    print(' '.join(map(str, result_pre_order)))

    result_post_order = []
    tree.post_order_traversal(0, result_post_order)
    print(' '.join(map(str, result_post_order)))
  

if __name__ == "__main__":
    threading.Thread(target=main).start()
