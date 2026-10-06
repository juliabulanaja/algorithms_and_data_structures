# python3
# Task. Find all occurrences of a given collection of patterns in a string.

# def construct_suffix_array(string: str) -> list:
#     order = sort_characters(string)
#     classes = compute_char_classes(string, order)
#     l = 1
#     while l < len(string):
#         order = sort_doubled(string, l, order, classes)
#         classes = update_classes(order, classes, l)
#         l = l * 2
#     return order


def sort_characters(string: str) -> list:
    n = len(string)
    alphabet_size = 256
    order = [None] * n
    count = [0] * alphabet_size

    # Count occurrences of each character
    for char in string:
        count[ord(char)] += 1

    # Compute cumulative counts
    for j in range(1, alphabet_size):
        count[j] += count[j - 1]

    # Place characters in order array from right to left
    for i in range(len(string) - 1, -1, -1):
        c = ord(string[i])
        count[c] -= 1
        order[count[c]] = i

    return order


def compute_char_classes(string: str, order: list) -> list:
    n = len(string)
    classes = [None] * n
    classes[order[0]] = 0

    for i in range(1, n):
        if string[order[i]] != string[order[i - 1]]:
            classes[order[i]] = classes[order[i - 1]] + 1
        else:
            classes[order[i]] = classes[order[i - 1]]
    # print(classes)
    return classes


def sort_doubled(string: str, l: int, order: list, classes: list) -> list:
    n = len(string)
    count = [0] * n
    new_order = [None] * n
    for i in range(n):
        count[classes[i]] = count[classes[i]] + 1

    for j in range(1, n):
        count[j] = count[j] + count[j - 1]

    for i in range(n - 1, -1, -1):
        start = (order[i] - l + n) % n
        cl = classes[start]
        count[cl] = count[cl] - 1
        new_order[count[cl]] = start
    
    return new_order


def update_classes(new_order: list, classes: list, l: int) -> list:
    n = len(new_order)
    new_classes = [None] * n
    new_classes[new_order[0]] = 0

    for i in range(1, n):
        cur = new_order[i]
        prev = new_order[i - 1]

        mid = (cur + l) % n
        mid_prev = (prev + l) % n

        if classes[cur] != classes[prev] or classes[mid] != classes[mid_prev]:
            new_classes[cur] = new_classes[prev] + 1
        else:
            new_classes[cur] = new_classes[prev]
    
    return new_classes
 

# def LCP_of_suffixes(string, i, j, equal):
#     lcp = max(0, equal)
#     while  i + lcp < len(string) and j + lcp < len(string):
#         if string[i + lcp] == string[j + lcp]:
#             lcp += 1
#         else:
#             break
#     return lcp


# def invert_suffix_array(order):
#     pos = [None] * len(order)
#     for i in range(len(order)):
#         pos[order[i]] = i
#     return pos


# def compute_LCP_array(string, order):
#     n = len(string) - 1
#     lcp_array = [None] * n
#     lcp = 0
#     pos_in_order = invert_suffix_array(order)
#     suffix = order[0]

#     for i in range(n):
#         order_index = pos_in_order[suffix]
#         if order_index == n:
#             lcp = 0
#             suffix = (suffix + 1) % (n + 1)
#             continue
#         next_suffix = order[order_index + 1]
#         lcp = LCP_of_suffixes(string, suffix, next_suffix, lcp - 1)
#         lcp_array[order_index] = lcp
#         suffix = (suffix + 1) % (n + 1)

#     return lcp_array

class SuffixTreeNode:
    def __init__(self, parent, children, string_depth, edge_start, edge_end):
        self.parent = parent
        self.children = children
        self.string_depth = string_depth
        self.edge_start = edge_start
        self.edge_end = edge_end

# def ST_from_SA(string, order, lcp_array):
#     root = SuffixTreeNode(parent=None, children={}, string_depth=0, edge_start=-1, edge_end=-1)
#     lpc_prev = 0
#     cur_node = root

#     for i in range(len(string)):
#         suffix = order[i]
#         while cur_node.string_depth > lpc_prev:
#             cur_node = cur_node.parent
#         if cur_node.string_depth == lpc_prev:
#             cur_node = create_new_leaf(cur_node, string, suffix)
#         else:
#             edge_start = order[i - 1] + cur_node.string_depth
#             offset = lpc_prev - cur_node.string_depth
#             min_node = break_edge(cur_node, string, edge_start, offset)
#             cur_node = create_new_leaf(min_node, string, suffix)
#         if i < len(string) - 1:
#             lpc_prev = lcp_array[i]

#     return root

# def create_new_leaf(node, string, suffix):
#     n = len(string)
#     leaf = SuffixTreeNode(
#         parent = node, 
#         children={}, 
#         string_depth = n-suffix, 
#         edge_start = suffix+node.string_depth,
#         edge_end = n - 1
#     )
#     node.children[string[leaf.edge_start]] = leaf 

#     return leaf

# def break_edge(node, string, start, offset):
#     start_char = string[start]
#     mid_char = string[start + offset]
#     mid_node = SuffixTreeNode(
#         children={},
#         parent=node,
#         string_depth=node.string_depth + offset,
#         edge_start=start,
#         edge_end=start + offset - 1
#     )
#     mid_node.children[mid_char] = node.children[start_char]
#     node.children[start_char].parent = mid_node
#     node.children[start_char].edge_start += offset
#     node.children[start_char] = mid_node

#     return mid_node


def find_pattern(text, pattern, order):
    min_index = 0
    max_index = len(order)

    # Find the left boundary
    while min_index < max_index:
        mid = (min_index + max_index) // 2
        suffix = text[order[mid]:]

        if suffix < pattern:
            min_index = mid + 1
        else:
            max_index = mid

    start = min_index

    # Find the right boundary
    max_index = len(order)

    while min_index < max_index:
        mid = (min_index + max_index) // 2
        suffix = text[order[mid]:]

        if suffix.startswith(pattern):
            min_index = mid + 1
        elif suffix < pattern:
            min_index = mid + 1
        else:
            max_index = mid

    return order[start:min_index]


if __name__ == "__main__":
    string = input()
    n = int(input())
    patterns = input().split(" ")

    string += "$"

    order = sort_characters(string)
    classes = compute_char_classes(string, order)

    length = 1
    while length < len(string):
        order = sort_doubled(string, length, order, classes)
        classes = update_classes(order, classes, length)
        length *= 2

    # Exclude the suffix consisting only of '$'
    order = order[1:]

    result = []
    seen = set()

    for pattern in patterns:
        for position in find_pattern(string, pattern, order):
            if position not in seen:
                seen.add(position)
                result.append(position)

    print(*result)

