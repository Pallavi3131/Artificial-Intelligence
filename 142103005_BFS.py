graph = {
    'O': ['B', 'E'],
    'B': ['O', 'C', 'E'],
    'C': ['B', 'X', 'E'],
    'X': ['C', 'E'],
    'E': ['B', 'C', 'X'],
}


def Succesor(N, space):
    return space[N]


def Goal_Test(N, Goal):
    if N == Goal:
        return True
    else:
        return False


def BFS(space, start, goal):
    open_list = [start]
    path = []

    while open_list:
        element = open_list.pop(0)

        if element not in path:
            path.append(element)

        if Goal_Test(element, goal):
            return path
        else:
            childern = Succesor(element, space)
            for child in childern:
                if child not in path:
                    open_list.append(child)

    return path


start = 'O'
goal = 'X'

print(" The Breadth First Search : ")
print(BFS(graph, start, goal))