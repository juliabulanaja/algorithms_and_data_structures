# python3
# Task. Find the shortest substring of one string that does not appear in another string.
# Input: Strings Text1 and Text2.
# Output: The shortest (non-empty) substring of Text1 that does not appear in Text2.
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

    def __repr__(self):
        return "{}".format(self.value)


class SuffixTrie:
    def __init__(self, text: str):
        self.root = SuffixTreeNode('')
        self.construct_suffix_tree(text)

    def __repr__(self):
        return "root: 0"

    def construct_suffix_tree(self, text: str):

        for i, start_symbol in enumerate(text):
            node = self.root
            j = i

            while node and j < len(text):
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
                    next_node.children = [old_node]

                    if new_suffix:
                        new_node = SuffixTreeNode(new_suffix)
                        next_node.children.append(new_node)
                    break
                        
               
                node = next_node
                j += k

        return self

    def path_exists(self, text: str) -> bool:
        node = self.root
        i = 0
        n = len(text)

        while i < n:
            for child in node.children:
                child_len = len(child.value)
                
                if child_len >= n - i and child.value.startswith(text[i:n]):
                    return True
    
                elif child_len < n - i and child.value == text[i:i+child_len]:
                    i += child_len
                    node = child
                    break
            else:
                return False
                
        return True

    
def find_shortest_unique_substring(trie1: SuffixTrie, trie2: SuffixTrie) -> str:

    q = Queue()
    q.put((trie1.root, '', 0))

    while not q.empty():
        node, curr_str, n = q.get()

        if n < len(node.value):
            next_symbol = node.value[n]
            string = curr_str + next_symbol
            path_exists = trie2.path_exists(string)
            if not path_exists:
                return string
            q.put((node, string, n + 1))
            continue
            
        for child in node.children:
            child_str = child.value
            string = curr_str + child_str[0]
            path_exists = trie2.path_exists(string)
            if not path_exists:
                return string
            q.put((child, string, 1))

    return string


if __name__ == "__main__":
    string1 = input().strip()
    string2 = input().strip()
   
    trie1 = SuffixTrie(string1)
    trie2 = SuffixTrie(string2)
    result = find_shortest_unique_substring(trie1, trie2)
    print(result)