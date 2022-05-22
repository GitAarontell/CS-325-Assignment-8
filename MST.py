def Prims(G):
    # set the unvisited vertices count to n -1
    vertices = len(G) - 1
    # set vertex 0 into visited list
    visited = [0]
    path = []

    while vertices != 0:
        lowestE = float('infinity')
        index = -1
        parent = -1
        for i in visited:
            # get lowest value in each node's neighbors in visited array
            temp_lowestE, temp_index = primMin(G[i])
            # get the lowest value edge in all the visited nodes
            if temp_lowestE < lowestE:
                lowestE = temp_lowestE
                index = temp_index
                parent = i
        vertices -= 1
        path.append((parent, index, lowestE))
        visited.append(index)
        # get rid of node in parent array
        G[parent][index] = 0
    return path


# have to return [(v1, v2, weight)] an array of tuples that was your path


def primMin(arr):
    minimum = float('infinity')
    index = -1
    for i in range(len(arr)):
        if arr[i] != 0 and arr[i] < minimum:
            minimum = arr[i]
            index = i

    return minimum, index


if __name__ == '__main__':
    g = [1, 2, 3]
    Prims(g)
