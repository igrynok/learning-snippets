from collections import deque


def is_landlocked(cell, grid):

    rows = len(grid)
    columns = len(grid[0])

    if grid[cell[0]][cell[1]] == 1:
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for direction in dirs:
            if 0 <= cell[0] + direction[0] < rows and 0 <= cell[1] + direction[1] < columns:
                if grid[cell[0] + direction[0]][cell[1] + direction[1]] == 1:
                    continue
                else:
                    return False
        return True
    else:
        return False


def get_neighbours(current, grid, landlocked):

    rows = len(grid)
    columns = len(grid[0])

    neighbours = []
    dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    for direction in dirs:
        if 0 <= current[0] + direction[0] < rows and 0 <= current[1] + direction[1] < columns:
            if grid[current[0] + direction[0]][current[1] + direction[1]] == 1:
                neighbours.append((current[0] + direction[0], current[1] + direction[1]))

    return neighbours


def bfs(cell, landlocked, visited, grid):
    queue = deque(cell)
    area = 1
    while queue:
        current = queue.pop()
        for neighbour in get_neighbours(current, grid, landlocked):
            if neighbour in visited:
                continue
            visited.add(neighbour)
            queue.append(neighbour)
            area += 1
    return area


def continent_size_with_largest_landlocked_area(grid):

    rows = len(grid)
    columns = len(grid[0])

    max_area = -1
    max_cell = (-1, -1)
    visited = set()

    for row in range(rows):
        for column in range(columns):
            if (row, column) in visited or not is_landlocked((row, column), grid):
                continue
            visited.add((row, column))
            area = bfs((row, column), True, visited, grid)
            if area > max_area:
                max_area = area
                max_cell = (row, column)

    if max_area != -1:
        visited = set()
        return bfs(max_cell, False, visited, grid)
    else:
        return -1
