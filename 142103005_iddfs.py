graph = {
    1: [2, 3],
    2: [1, 6],
    3: [4],
    4: [3, 8],
    5: [6, 7],
    6: [5],
    7: [8],
    8: [7]
}
path = []

def DFS_search(start, goal, graph, maximum_depth, current_list):

    current_list.append(start)
    if start == goal:
        return True
    if maximum_depth <= 0:
        path.append(current_list)
        return False
    for node in graph[start]:
        if DFS_search(node, goal, graph, maximum_depth-1, current_list):
            return True
        else:
            current_list.pop()
    return False

def IDDFS_search_search(start, goal, graph, max_depth):
    for i in range(max_depth):
        current_list = []
        if DFS_search(start, goal, graph, i, current_list):
            return True
    return False
if not IDDFS_search_search(1, 4, graph, 6):
    print("The Path is unavailable")
else:
    print("The Path: ", path[-1])
