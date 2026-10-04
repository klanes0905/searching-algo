GRID = [
    "S....#....",
    ".##..#....",
    ".#...#....",
    ".#.......#",
    ".#####...#",
    ".........G"
]

START = (0, 0)
GOAL = (5, 9)

ROWS = len(GRID)
COLS = len(GRID[0])

DIRECTIONS = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]


def is_valid(position):
    row, col = position
    return (
        0 <= row < ROWS
        and 0 <= col < COLS
        and GRID[row][col] != "#"
    )


def reconstruct_path(parent, start, goal):
    if goal != start and goal not in parent:
        return []

    path = []
    current = goal

    while current is not None:
        path.append(current)

        if current == start:
            break

        current = parent.get(current)

    path.reverse()
    return path if path and path[0] == start else []


def draw_grid(path):
    path_set = set(path)

    for row in range(ROWS):
        line = ""

        for col in range(COLS):
            position = (row, col)

            if position == START:
                line += "S"
            elif position == GOAL:
                line += "G"
            elif position in path_set:
                line += "*"
            elif GRID[row][col] == "#":
                line += "#"
            else:
                line += "."

        print(line)

import heapq


# ==========================================
# A* SEARCH
# ==========================================

def heuristic(position, goal):
    # Manhattan distance:
    # |row1 - row2| + |column1 - column2|
    return abs(position[0] - goal[0]) + abs(position[1] - goal[1])


def a_star(start, goal):
    # Priority queue stores:
    # (f_score, counter, position)
    open_set = []

    counter = 0
    heapq.heappush(open_set, (0, counter, start))

    parent = {start: None}
    g_score = {start: 0}
    visited = set()

    while open_set:
        _, _, current = heapq.heappop(open_set)

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return reconstruct_path(parent, start, goal), visited

        for dr, dc in DIRECTIONS:
            neighbor = (current[0] + dr, current[1] + dc)

            if not is_valid(neighbor):
                continue

            # Cost of moving to a neighboring cell is 1
            tentative_g = g_score[current] + 1

            if tentative_g < g_score.get(neighbor, float("inf")):
                parent[neighbor] = current
                g_score[neighbor] = tentative_g

                # f(n) = g(n) + h(n)
                f_score = tentative_g + heuristic(neighbor, goal)

                counter += 1
                heapq.heappush(
                    open_set,
                    (f_score, counter, neighbor)
                )

    return [], visited


# ==========================================
# RUN A*
# ==========================================

if __name__ == "__main__":
    path, visited = a_star(START, GOAL)

    print("A* SEARCH")
    print("=" * 40)

    print("\nOriginal Grid:")
    for row in GRID:
        print(row)

    if path:
        print("\nPath Found!")
        print("Path length:", len(path) - 1)
        print("Nodes visited:", len(visited))
        print("Path:", path)

        print("\nA* Result:")
        draw_grid(path)
    else:
        print("\nNo path found.")
