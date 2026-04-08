from models.heap import MinHeap

def dijkstra(graph, start, end):
    heap = MinHeap()
    heap.insert((0, start))  # (distance, node)

    distances = {}
    parent = {}

    # Initialize distances
    for node in graph.adj_list:
        distances[node] = float('inf')

    distances[start] = 0

    while not heap.is_empty():
        current_distance, current_node = heap.extract_min()

        # If reached destination
        if current_node == end:
            break

        for neighbor, weight in graph.adj_list[current_node]:
            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                parent[neighbor] = current_node

                heap.insert((new_distance, neighbor))

    path = []
    node = end

    while node != start:
        path.append(node)
        node = parent.get(node)

        if node is None:
            return None

    path.append(start)
    path.reverse()

    return path, distances[end]