from maze_logic import build_graph, find_start_end
from algorithms.bfs import bfs

graph = build_graph()
start, end = find_start_end()

path = bfs(graph, start, end)

print("Path", path)


