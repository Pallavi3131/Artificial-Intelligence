graph = {
    'X': ['O', 'H'],
    'O': ['X', 'C', 'H'],
    'C': ['O', 'D', 'H'],
    'D': ['C', 'H'],
    'H': ['O', 'C', 'D'],
}


def Succesor(N, space):
    return space[N]


def Goal_Test(N, Goal):
    if N == Goal:
        return True
    else:
        return False


def DFS(space, start, goal):
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
                    open_list.insert(0, child)

    return path


start = 'X'
goal = 'D'

print(" The Depth First Search : ")
print(DFS(graph, start, goal))