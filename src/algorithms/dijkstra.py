from models.heap import MinHeap


def dijkstra(graph, start, end):
    heap = MinHeap()
    heap.insert((0, start))

    distances = {}
    parent = {}

    for node in graph.adj_list:
        distances[node] = float('inf')

    if start not in distances:
        distances[start] = 0
    else:
        distances[start] = 0

    if end not in distances:
        distances[end] = float('inf')

    found = False

    while not heap.is_empty():
        current_data = heap.extract_min()
        if not current_data:
            break

        current_distance, current_node = current_data

        if current_node == end:
            found = True
            break

        for neighbor, weight in graph.adj_list.get(current_node, []):
            new_distance = current_distance + weight

            if new_distance < distances.get(neighbor, float('inf')):
                distances[neighbor] = new_distance
                parent[neighbor] = current_node
                heap.insert((new_distance, neighbor))

    if not found:
        return None

    path = []
    curr = end

    while curr is not None:
        path.append(curr)
        if curr == start:
            break
        curr = parent.get(curr)

    path.reverse()

    return path, distances[end]