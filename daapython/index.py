import heapq

def dijkstra(n, graph, source):
    # Initialize distances with infinity
    distances = [float('inf')] * (n + 1)
    distances[source] = 0  # Distance to the source is 0
    
    # Min-heap priority queue
    priority_queue = []
    heapq.heappush(priority_queue, (0, source))  # (distance, node)
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If the current distance is greater than the recorded distance, continue
        if current_distance > distances[current_node]:
            continue
        
        # Process each neighbor of the current node
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    # Convert infinite distances to -1 (unreachable nodes)
    return [-1 if dist == float('inf') else dist for dist in distances[1:]]

# Example usage:

# Number of nodes (vertices) and edges (edges)
n = 5
m = 6

# Adjacency list representation of the graph (node -> list of (neighbor, weight))
graph = {i: [] for i in range(1, n + 1)}

# Add edges (u, v, w) - from node u to v with weight w
edges = [
    (1, 2, 2),
    (1, 3, 4),
    (2, 3, 1),
    (2, 4, 7),
    (3, 5, 3),
    (4, 5, 1)
]

for u, v, w in edges:
    graph[u].append((v, w))
    graph[v].append((u, w))  # For undirected graph

# Set the source node
source = 1

# Get shortest distances from the source node to all other nodes
shortest_distances = dijkstra(n, graph, source)

# Output the result
print("Shortest distances from source:", shortest_distances)
