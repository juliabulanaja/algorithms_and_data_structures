# python3
# Task. Construct the suffix tree of a string.
from queue import Queue


class SuffixTreeNode:
    def __init__(self, value: str):
        self.value = value
        self.children = []

    def find_child(self, value: str):
        for child in self.children:
            if child.value.startswith(value):
                return child
        return None

    def add_child(self, new_node):
        self.children.append(new_node)

    # def __repr__(self):
    #     return f"{self.value}"


class SuffixTrie:
    def __init__(self, text: str):
        self.root = SuffixTreeNode(0)
        self.construct_suffix_tree(text)

    # def __repr__(self):
    #     return f"root: 0"

    def construct_suffix_tree(self, text: str):

        for i, start_symbol in enumerate(text):
            node = self.root
            j = i

            while node:
                current_substring = text[j:]
                next_node = node.find_child(text[j])

                if not next_node:
                    new_node = SuffixTreeNode(text[j:])
                    node.add_child(new_node)
                    break

                next_node_text = next_node.value
                k = 0
                while k < len(next_node_text) and j + k < len(text):

                    if next_node_text[k] != text[j + k]:
                        break
                    k += 1

                if k < len(next_node_text):

                    equal_part = next_node_text[:k]
                    old_suffix = next_node_text[k:]
                    new_suffix = text[j + k:]
                    
                    next_node.value = equal_part

                    old_node = SuffixTreeNode(old_suffix)
                    old_node.children = next_node.children

                    new_node = SuffixTreeNode(new_suffix)
                    next_node.children = [old_node, new_node]

                    break
                        
               
                node = next_node
                j += k

        return self

    def print_graph(self):
        q = Queue()
        q.put(self.root)
  
        while not q.empty():
            node = q.get()
            for neighbor in node.children:
                q.put(neighbor)
            if self.root != node:
                print(node.value)


if __name__ == "__main__":
    text = input()
    trie = SuffixTrie(text)
    trie.print_graph()
