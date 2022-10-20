graph = {'P': [('R', 1), ('I', 4), ('D', 5)],
         'R': [('Q', 8)],
         'I': [('D', 2)],
         'Q': [('D', 1), ('H', 2)],
         'D': [('H', 7)],
         'H': []}


def Path_cost(path):
    total = 0
    for (node, cost) in path:
        total += cost
    return total, path[-1][0]


def UCS(graph, start, goal):
    visited = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=Path_cost)
        print("OpenList : ", queue)
        print("ClosedList : ", visited)
        path = queue.pop(0)
        node = path[-1][0]
        print("Node : ", node)

        if node in visited:
            continue
        visited.append(node)
        if node == goal:
            print("Goal Achieved")
            return path
        else:
            print("Goal Not Achieved")
            adj = graph.get(node, [])
            for (node2, cost) in adj:
                current_path = path.copy()
                current_path.append((node2, cost))
                queue.append(current_path)


ans = UCS(graph, 'R', 'H')
print("Path: ", ans)
print("Path Cost: ", Path_cost(ans)[0])