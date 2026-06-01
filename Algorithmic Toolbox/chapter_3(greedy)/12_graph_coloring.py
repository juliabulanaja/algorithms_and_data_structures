# graph = {
#     0: [1, 2, 3, 4],
#     1: [0],
#     2: [0],
#     3: [0],
#     4: [0]}


graph = {
    0: [1, 2, 3],
    1: [0, 2, 3],
    2: [0, 1, 3],
    3: [0, 1, 2]
}

graph = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 5, 6],
    4: [2, 6],
    5: [2, 3, 7],
    6: [3, 4, 7],
    7: [5, 6]
}


def color_graph(graph: dict, node: int, node_colors: dict={}, colors: list=[]):

    children = graph.get(node, [])

    has_color = False

    children_colors = [node_colors.get(child, 0) for child in children] 
    for color in colors:
        if color not in children_colors:
            node_color = color
            has_color = True  
            break

    if not has_color:
        node_color = len(colors) + 1
        colors.append(node_color)

    node_colors[node] = node_color

    for child in children:
        if child not in node_colors:
            node_colors, colors = color_graph(graph, child, node_colors, colors)

    return node_colors, colors


node_colors, colors = color_graph(graph, 1)
print(len(colors))
print(node_colors)








