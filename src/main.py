import pygame
import sys
from maze_logic import build_graph, find_start_end, maze, CELL_SIZE
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra

pygame.init()

ROWS = len(maze)
COLS = len(maze[0])
WIDTH = COLS * CELL_SIZE
HEIGHT = ROWS * CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Maze Solver: AI Animation (SPACE to Toggle)")

# --- UPDATED COLORS ---
WHITE = (255, 255, 255)
BLACK = (20, 20, 20)
GREEN = (46, 204, 113)
RED = (231, 76, 60)
BLUE = (52, 152, 219)
YELLOW = (241, 196, 15)
CYAN = (52, 231, 228)
BROWN = (139, 69, 19)
WATER_BLUE = (0, 105, 148)

def draw_maze():
    for r in range(ROWS):
        for c in range(COLS):
            x = c * CELL_SIZE
            y = r * CELL_SIZE

            tile = maze[r][c]
            if tile == '#': color = BLACK
            elif tile == 'S': color = GREEN
            elif tile == 'E': color = RED
            elif tile == 'M': color = BROWN     # Mud tile
            elif tile == 'W': color = WATER_BLUE # Water tile
            else: color = WHITE

            pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))
            pygame.draw.rect(screen, BLUE, (x, y, CELL_SIZE, CELL_SIZE), 1)

def draw_path(path, color):
    if not path:
        return
    for (r, c) in path:
        if maze[r][c] not in ['S', 'E']:
            padding = CELL_SIZE // 4
            x = c * CELL_SIZE + padding
            y = r * CELL_SIZE + padding
            size = CELL_SIZE - (padding * 2)
            pygame.draw.rect(screen, color, (x, y, size, size))

def run_game():
    graph = build_graph()
    start, end = find_start_end()

    bfs_path = bfs(graph, start, end)
    d_result = dijkstra(graph, start, end)
    dijkstra_path = d_result[0] if d_result else None

    show_dijkstra = True
    current_step = 0
    frame_count = 0
    animation_speed = 8
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    show_dijkstra = not show_dijkstra
                    current_step = 0
                    frame_count = 0

        screen.fill(WHITE)
        draw_maze()

        path = dijkstra_path if show_dijkstra else bfs_path

        if path:
            frame_count += 1
            if frame_count % animation_speed == 0:
                if current_step < len(path):
                    current_step += 1

            animated_path = path[:current_step]
            color = YELLOW if show_dijkstra else CYAN
            draw_path(animated_path, color)

        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    run_game()