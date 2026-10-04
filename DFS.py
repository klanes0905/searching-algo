GRID = [
    "S....#....",
    ".##..#....",
    ".#...#....",
    ".#.......#",
    ".#########",
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


# ==========================================
# DEPTH-FIRST SEARCH (DFS)
# ==========================================

def dfs(start, goal):
    # DFS uses a stack: Last In, First Out
    stack = [start]

    visited = {start}
    parent = {start: None}

    while stack:
        current = stack.pop()

        if current == goal:
            return reconstruct_path(parent, start, goal), visited

        for dr, dc in DIRECTIONS:
            neighbor = (current[0] + dr, current[1] + dc)

            if is_valid(neighbor) and neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                stack.append(neighbor)

    return [], visited


# ==========================================
# RUN DFS
# ==========================================

if __name__ == "__main__":
    path, visited = dfs(START, GOAL)

    print("DEPTH-FIRST SEARCH (DFS)")
    print("=" * 40)

    print("\nOriginal Grid:")
    for row in GRID:
        print(row)

    if path:
        print("\nPath Found!")
        print("Path length:", len(path) - 1)
        print("Nodes visited:", len(visited))
        print("Path:", path)

        print("\nDFS Result:")
        draw_grid(path)
    else:
        print("\nNo path found.")
