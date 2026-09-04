# python3
# Task. Given a string Text and a collection of strings Patterns, find all starting positions in Text where any string from Patterns appears as a substring.

class TrieNode:

    def __init__(self, value: str, node_id: int = None):
        self.value = value
        self.children = {}
        self.end = False

    def add_child(self, node):
        self.children[node.value] = node
        return node

    def find_child(self, value: str):
        return self.children.get(value)


class Trie:
    def __init__(self, patterns: list):
        self.root = TrieNode(0, 0)
        self.construct_trie(patterns)
    
    def construct_trie(self, patterns: list) -> Trie:
        for pattern in patterns:
            current_node = self.root
            for symbol in pattern:
                if current_node.find_child(symbol) is not None:
                    current_node = current_node.find_child(symbol)
                else:
                    new_node = TrieNode(symbol)
                    current_node.add_child(new_node)
                    current_node = new_node
            current_node.end = True
        return self

def find_occurrences(text: str, trie: Trie) -> None:
    result = []

    for i in range(len(text)):
        node = trie.root

        for symbol in text[i:]:
            node = node.find_child(symbol)
            if node is None:
                break

            if node.end:
                result.append(i)

            if not node.children:
                result.append(i)
                break
           
    print(" ".join(map(str, sorted(set(result)))))


if __name__ == "__main__":
    text = input()
    n = int(input())
    patterns = []
    for _ in range(n):
        patterns.append(input())

trie = Trie(patterns)
find_occurrences(text, trie)

    