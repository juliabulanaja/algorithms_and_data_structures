class Node:
    def __init__(self, val):
        self._val = val
        self._children = []

    def add_child(self, node):
        self._children.append(node)

    def get_children(self):
        return self._children

    def get_value(self):
        return self._val
    
    def __repr__(self):
        return str(self._val)


class Tree:
    def __init__(self, data):
        self._root = Node(data[0])
        self.create_tree(self._root, data[1:])
        # self.print_tree(self._root)
    
    def get_root(self):
        return self._root

    def create_tree(self, node, data):
  
        child = None
        for item in data:
            
            if isinstance(item, list):
                if child:
                    self.create_tree(child, item)
                else:
                    self.create_tree(node, item)
            else:
                child = Node(item)
                node.add_child(child)

    def print_tree(self, node, level=0):
        print("  " * level + str(node._val))
        for child in node._children:
            self.print_tree(child, level + 1)


def solve_problem(tree: Tree):
    root = tree.get_root()

    def inner(node):
        node_value = node.get_value()
        children = node.get_children()
        
        take = node_value
        skip = 0

        take_nodes = [node]
        skip_nodes = []
        
        for child in children:
            take_child, skip_child, t_nodes, s_nodes = inner(child)
            take += skip_child
            take_nodes.extend(s_nodes)

            if take_child >= skip_child:
                skip += take_child
                skip_nodes.extend(t_nodes)
            else:
                skip += skip_child
                skip_nodes.extend(s_nodes)

        return take, skip, take_nodes, skip_nodes

    take, skip, take_nodes, skip_nodes = inner(root)
    # print(take, skip, take_nodes, skip_nodes)
    if take >= skip:
        return take_nodes

    return skip_nodes


if __name__ == "__main__":
    data = [3, [5, [2], 1, [3], 6, [7, [1, 2, 1], 2]]]
    tree = Tree(data)

    result = solve_problem(tree)
    print(result)