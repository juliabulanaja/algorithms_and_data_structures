# python3
# Task. Construct a trie from a collection of patterns.
from queue import Queue


class Trie:
    def __init__(self, patterns: list):
        self.root = TrieNode(0, 0)
        self.node_counter = 1
        self.construct_trie(patterns)
    
    def construct_trie(self, patterns: list):
        for pattern in patterns:
            current_node = self.root
            for symbol in pattern:
                if current_node.find_child(symbol) is not None:
                    current_node = current_node.find_child(symbol)
                else:
                    new_node = TrieNode(symbol, self.node_counter)
                    current_node.add_child(new_node)
                    current_node = new_node
                    self.node_counter += 1
        return self

    def print_trie(self) -> None:
        q = Queue()
        q.put((self.root))

        while not q.empty():
            node = q.get()
            for child in node.children.values():
                print("{0}->{1}:{2}".format(node.node_id, child.node_id, child.value))
                q.put((child))

    
class TrieNode:

    def __init__(self, value: str, node_id: int = None):
        self.value = value
        self.node_id = node_id
        self.children = {}

    def add_child(self, node):
        self.children[node.value] = node
        return node

    def find_child(self, value: str):
        return self.children.get(value)


if __name__ == "__main__":
    n = int(input())
    patterns = []
    for _ in range(n):
        patterns.append(input())

    trie = Trie(patterns)
    trie.print_trie()
