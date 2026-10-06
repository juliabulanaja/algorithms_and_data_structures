# python3
# Task. Construct a suffix tree from the suffix array and LCP array of a string.

import sys


class SuffixTreeNode:
    def __init__(self, parent, string_depth, edge_start, edge_end, suffix_index=-1):
        self.parent = parent
        self.children = {}
        self.string_depth = string_depth
        self.edge_start = edge_start
        self.edge_end = edge_end
        self.suffix_index = suffix_index


def create_new_leaf(node, string, suffix):
    leaf = SuffixTreeNode(
        parent=node,
        string_depth=len(string) - suffix,
        edge_start=suffix + node.string_depth,
        edge_end=len(string) - 1,
        suffix_index=suffix,
    )
    start_char = string[leaf.edge_start]
    node.children[start_char] = leaf
    return leaf


def break_edge(node, string, start, offset):
    start_char = string[start]
    child = node.children[start_char]

    mid_node = SuffixTreeNode(
        parent=node,
        string_depth=node.string_depth + offset,
        edge_start=start,
        edge_end=start + offset - 1,
    )

    child.edge_start += offset
    mid_char = string[child.edge_start]

    mid_node.children[mid_char] = child
    child.parent = mid_node

    node.children[start_char] = mid_node
    return mid_node


def ST_from_SA(string, order, lcp_array):
    root = SuffixTreeNode(parent=None, string_depth=0, edge_start=-1, edge_end=-1)
    lcp_prev = 0
    cur_node = root

    for i in range(len(string)):
        suffix = order[i]
        while cur_node.string_depth > lcp_prev:
            cur_node = cur_node.parent

        if cur_node.string_depth == lcp_prev:
            cur_node = create_new_leaf(cur_node, string, suffix)
        else:
            edge_start = order[i - 1] + cur_node.string_depth
            offset = lcp_prev - cur_node.string_depth
            min_node = break_edge(cur_node, string, edge_start, offset)
            cur_node = create_new_leaf(min_node, string, suffix)

        if i < len(string) - 1:
            lcp_prev = lcp_array[i]

    return root


def calculate_min_rank(root, order):
    rank = {suffix: i for i, suffix in enumerate(order)}
    min_rank = {}

    # Iterative Post-Order Traversal to compute min_rank safely
    post_order = []
    stack = [root]
    while stack:
        node = stack.pop()
        post_order.append(node)
        for child in node.children.values():
            stack.append(child)

    # Process nodes bottom-up
    for node in reversed(post_order):
        if not node.children:
            min_rank[node] = rank[node.suffix_index]
        else:
            min_rank[node] = min(min_rank[child] for child in node.children.values())

    return min_rank


def print_edges(root, order):
    min_rank = calculate_min_rank(root, order)

    # Iterative Pre-Order (DFS) Traversal to print edges
    stack = [root]
    while stack:
        node = stack.pop()
        if node != root:
            print("%d %d" % (node.edge_start, node.edge_end + 1))

        # Sort children in REVERSE order so the smallest min_rank pops first
        sorted_children = sorted(
            node.children.values(), key=lambda c: min_rank[c], reverse=True
        )
        for child in sorted_children:
            stack.append(child)


if __name__ == "__main__":
    string = sys.stdin.readline().strip()
    order = list(map(int, sys.stdin.readline().split()))
    lcp_array = list(map(int, sys.stdin.readline().split()))

    root = ST_from_SA(string, order, lcp_array)

    print(string)
    print_edges(root, order)
    