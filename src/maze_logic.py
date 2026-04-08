from models.graph import Graph

# S=Start, E=End, #=Wall, M=Mud, W=Water
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
                            weight = 10
                        elif target_tile == 'M':
                            weight = 5
                        else:
                            weight = 1

                        graph.add_edge(current, neighbor, weight)
    return graph