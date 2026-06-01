#!/usr/bin/python3
import sys, threading


class Tree:
    def __init__(self, verticies):
        self.key = list(map(lambda x: x[0], verticies))
        self.left = list(map(lambda x: x[1], verticies))
        self.right = list(map(lambda x: x[2], verticies))


    def is_bst_with_recursion(self, i=0, left_border=float('-inf'), right_border=float('inf')):
        if i == -1 or len(self.key) == 0:
            return True

        if self.key[i] < left_border or self.key[i] >= right_border:
            return False
        
        return (self.is_bst(self.left[i], left_border, self.key[i]) and 
                self.is_bst(self.right[i], self.key[i], right_border))

    
    def is_bst(self):
        if len(self.key) == 0:
            return True

        stack = [(0, float("-inf"), float("inf"))]

        while stack:
            i, start, end = stack.pop()
            if i == -1:
                continue

            node = self.key[i]

            if node < start or node >= end:
                return False

            stack.append((self.left[i], start, node))
            stack.append((self.right[i], node, end))

        return True
        

    def check_if_binary(self):
        return 'CORRECT' if self.is_bst() else 'INCORRECT'


def main():
    nodes = int(sys.stdin.readline().strip())
    verticies = []
    for i in range(nodes):
        verticies.append(list(map(int, sys.stdin.readline().strip().split())))

    tree = Tree(verticies)
    print(tree.check_if_binary())


threading.Thread(target=main).start()
