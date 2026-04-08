from models.graph import Graph

# M = Mud, W = Water
maze = [
    ['S', '.', 'W', '.'],
    ['.', 'W', '.', '.'],
    ['.', 'M', '.', 'E']
]

rows = len(maze)
cols = len(maze[0])
CELL_SIZE = 80

def is_valid(r, c):
    return 0 <= r < rows and 0 <= c < cols and maze[r][c] != '#'


def find_start_end():
    start, end = None, None
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
    return start, end


def build_graph():
    graph = Graph()
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] != '#':
                current = (r, c)
                graph.add_node(current)
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_valid(nr, nc):
                        neighbor = (nr, nc)

                        target_tile = maze[nr][nc]
                        if target_tile == 'W':
                            weight = 10  # High cost
                        elif target_tile == 'M':
                            weight = 5  # Medium cost
                        else:
                            weight = 1  # Low cost

                        graph.add_edge(current, neighbor, weight)
    return graph


def display_maze(maze, path=None):
    for r in range(len(maze)):
        for c in range(len(maze[0])):
            if path and (r, c) in path and maze[r][c] not in ['S', 'E']:
                print('*', end=' ')
            else:
                print(maze[r][c], end=' ')
        print()