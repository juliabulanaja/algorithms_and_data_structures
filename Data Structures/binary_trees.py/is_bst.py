#!/usr/bin/python3
import sys, threading


sys.setrecursionlimit(10**7) 
threading.stack_size(2**25) 


class Tree:
    def __init__(self, verticies):
        self.key = list(map(lambda x: x[0], verticies))
        self.left = list(map(lambda x: x[1], verticies))
        self.right = list(map(lambda x: x[2], verticies))
        self.parent = [None] * len(self.key)
        self.start = [float('-inf')] * len(self.key)
        self.end = [float('inf')] * len(self.key)
        self.set_parent()
 
    def find(self, node, i=0):
        
        current_node = self.key[i]
        if i == -1:
            return False
        if node == current_node:
            return True
        elif node < current_node:
            return self.find(node, self.left[i])
        else:
            return self.find(node, self.right[i])

    def set_parent(self):
        if len(self.key) == 0:
            return 
        
        for i in range(len(self.key)):
            left = self.left[i]
            right = self.right[i]

            if left >= 0:
                self.parent[left] = i
            if right >= 0:
                self.parent[right] = i


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

        for i in range(1, len(self.key)):
            current_value = self.key[i]
            parent_index = self.parent[i]
            parent_value = self.key[parent_index]

            if i == self.left[parent_index] and current_value < parent_value and current_value > self.start[parent_index]:
                self.start[i] = self.start[parent_index]
                self.end[i] = parent_value
            
            elif i == self.right[parent_index] and current_value >= parent_value and current_value < self.end[parent_index]:
                self.start[i] = parent_value
                self.end[i] = self.end[parent_index]
            else:
                return False

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
