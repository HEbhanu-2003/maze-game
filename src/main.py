from maze_logic import build_graph, find_start_end
from algorithms.bfs import bfs
from algorithms.dijkstra import dijkstra

def main():
    graph = build_graph()
    start, end = find_start_end()

    print("Start:", start)
    print("End:", end)

    bfs_path = bfs(graph, start, end)
    print("\nBFS Path:", bfs_path)
    if bfs_path:
        print("Steps (BFS):", len(bfs_path) - 1)

    dijkstra_result = dijkstra(graph, start, end)

    if dijkstra_result:
        dijkstra_path, cost = dijkstra_result
        print("\nDijkstra Path:", dijkstra_path)
        print("Total Cost:", cost)
    else:
        print("\nNo path found using Dijkstra")


if __name__ == "__main__":
    main()