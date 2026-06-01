import random 


tree = {
    1: {2, 3, 4}, 
    2: {5, 6}, 
    3: {7},
    7: {10, 11, 12}
}

def create_random_tree(n_nodes):
    tree = {}
    nodes_in_tree = [1] 
    
    for next_node in range(2, n_nodes + 1):
        parent = random.choice(nodes_in_tree)
        
        if parent not in tree:
            tree[parent] = {next_node}
        else:
            tree[parent].add(next_node)
            
        nodes_in_tree.append(next_node)
        
    return tree


def plan_party(tree: dict, node: int, include: list=[], exclude: list=[]):

    children = tree.get(node, [])

    include.append(node)

    for child in children:
        exclude.append(child)

        grandchilren = tree.get(child, [])
        for grandchild in grandchilren:
            plan_party(tree, grandchild, include, exclude)

    return include, exclude


def plan_party2(tree: dict, node: int): # O(n)

    included = 1
    excluded = 0
    children = tree.get(node, [])
  
    for child in children:
        
        child_included, child_excluded = plan_party2(tree, child)
        included += child_excluded
        excluded += max(child_included, child_excluded)

    return included, excluded

result = plan_party2(tree, 1)
print(max(result))
