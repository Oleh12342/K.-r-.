import heapq

# Заданий граф
graph = {
    1: [(2, 13), (7, 15)],
    2: [(1, 13), (3, 22), (8, 19)],
    3: [(2, 22), (4, 28), (9, 26)],
    4: [(3, 28), (5, 12), (10, 8)],
    5: [(4, 12), (6, 9), (11, 3)],
    6: [(5, 9), (12, 22)],
    7: [(1, 15), (8, 15), (13, 18)],
    8: [(2, 19), (7, 15), (9, 22), (14, 12)],
    9: [(3, 26), (8, 22), (10, 15), (15, 21)],
    10: [(4, 8), (9, 15), (11, 30), (16, 6)],
    11: [(5, 3), (10, 30), (12, 9), (17, 29)],
    12: [(6, 22), (11, 9), (18, 22)],
    13: [(7, 18), (14, 15), (19, 25)],
    14: [(8, 12), (13, 15), (15, 1), (20, 20)],
    15: [(9, 21), (14, 1), (16, 15), (21, 15)],
    16: [(10, 6), (15, 15), (17, 9), (22, 30)],
    17: [(11, 29), (16, 9), (18, 27), (23, 20)],
    18: [(12, 22), (17, 27), (24, 24)],
    19: [(13, 25), (20, 5), (25, 9)],
    20: [(14, 20), (19, 5), (21, 19), (26, 9)],
    21: [(15, 15), (20, 19), (22, 23), (27, 1)],
    22: [(16, 30), (21, 23), (23, 17), (28, 20)],
    23: [(17, 20), (22, 17), (24, 19), (29, 16)],
    24: [(18, 24), (23, 19), (30, 25)],
    25: [(19, 9), (26, 15), (31, 21)],
    26: [(20, 9), (25, 15), (27, 10), (32, 26)],
    27: [(21, 1), (26, 10), (28, 6), (33, 5)],
    28: [(22, 20), (27, 6), (29, 13), (34, 9)],
    29: [(23, 16), (28, 13), (30, 27), (35, 29)],
    30: [(24, 25), (29, 27), (36, 28)],
    31: [(25, 21), (32, 11), (37, 3)],
    32: [(26, 26), (31, 11), (33, 21), (38, 11)],
    33: [(27, 5), (32, 21), (34, 24), (39, 14)],
    34: [(28, 9), (33, 24), (35, 17), (40, 3)],
    35: [(29, 29), (34, 17), (36, 28), (41, 17)],
    36: [(30, 28), (35, 28), (42, 3)],
    37: [(31, 3), (38, 27), (43, 9)],
    38: [(32, 11), (37, 27), (39, 7), (44, 9)],
    39: [(33, 14), (38, 7), (40, 29), (45, 8)],
    40: [(34, 3), (39, 29), (41, 21), (46, 15)],
    41: [(35, 17), (40, 21), (42, 16), (47, 24)],
    42: [(36, 3), (41, 16), (48, 9)],
    43: [(37, 9), (44, 25)],
    44: [(38, 9), (43, 25), (45, 16)],
    45: [(39, 8), (44, 16), (46, 15)],
    46: [(40, 15), (45, 15), (47, 22)],
    47: [(41, 24), (46, 22), (48, 26)],
    48: [(42, 9), (47, 26)],
}

# Алгоритм Дейкстри
def dijkstra_with_weights(graph, start, end):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    min_heap = [(0, start)]
    edge_weights = {}  # Зберігає ваги для ребер

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                edge_weights[(current_node, neighbor)] = weight
                heapq.heappush(min_heap, (distance, neighbor))

    # Відновлення шляху з вагами
    path = []
    weights_path = []
    current = end

    while current != start:
        parent = previous_nodes[current]
        path.append((parent, current))
        weights_path.append(edge_weights[(parent, current)])
        current = parent

    weights_path.reverse()
    return distances[end], weights_path

# Виконання
def main():
    start = 1
    end = 48
    total_distance, weights_path = dijkstra_with_weights(graph, start, end)
    weights_path = ["початок"] + weights_path + ["кінець"]
    print(f"Загальна відстань: {total_distance}")
    print(f"Шлях: {' -> '.join(map(str, weights_path))}")

main()
