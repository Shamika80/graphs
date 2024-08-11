import heapq
class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = {}

    def add_edge (self,  
 source, destination, weight): 
        if source in self.vertices and destination in self.vertices:
            self.vertices[source][destination] = weight
            self.vertices[destination][source] = weight  # For undirected graph

    def get_neighbors(self, vertex):
        if vertex in self.vertices:
            return self.vertices[vertex]
        else:
            return {}

def dijkstra(graph, source):
    
    distances = {vertex: float('inf') for vertex in graph.vertices}
    distances[source] = 0
    paths = {vertex: [] for vertex in graph.vertices}
    priority_queue = [(0, source)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]: 

            continue

        for neighbor, weight in graph.get_neighbors(current_vertex).items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_vertex]+ [neighbor] 
                heapq.heappush (priority_queue, 
 (distance, neighbor)) 

    return distances, paths

# Test Case 1: Simple Linear Graph
graph1 = Graph()
graph1.add_vertex('A')
graph1.add_vertex('B')
graph1.add_vertex('C')
graph1.add_vertex('D')
graph1.add_edge('A', 'B', 2)
graph1.add_edge('B', 'C', 3)
graph1.add_edge('C', 'D', 1)

source_node1 = 'A'
distances1, paths1 = dijkstra(graph1, source_node1)

print("\n--- Test Case 1: Simple Linear Graph ---")
print("Shortest distances from node", source_node1, ":", distances1)
print("Shortest paths from node", source_node1, ":", paths1)

# Test Case 2: Graph with a Cycle
graph2 = Graph()
graph2.add_vertex('A')
graph2.add_vertex('B')
graph2.add_vertex('C')
graph2.add_vertex('D')
graph2.add_edge('A', 'B', 2)
graph2.add_edge('B', 'C', 3)
graph2.add_edge('C', 'D', 1)
graph2.add_edge('D', 'A', 4)

source_node2 = 'A'
distances2, paths2 = dijkstra(graph2, source_node2)

print("\n--- Test Case 2: Graph with a Cycle ---")
print("Shortest distances from node", source_node2, ":", distances2)
print("Shortest paths from node", source_node2, ":", paths2)

# Test Case 3: Disconnected Graph
graph3 = Graph()
graph3.add_vertex('A')
graph3.add_vertex('B')
graph3.add_vertex('C')
graph3.add_vertex('D')
graph3.add_edge('A', 'B', 2)
graph3.add_edge('C', 'D', 1)

source_node3 = 'A'
distances3, paths3 = dijkstra(graph3, source_node3)

print("\n--- Test Case 3: Disconnected Graph ---")
print("Shortest distances from node", source_node3, ":", distances3)
print("Shortest paths from node", source_node3, ":", paths3)

# Complexity Analysis
print("\n--- Complexity Analysis ---")
print("Time Complexity: O(V^2) for dense graphs, can be improved to O((V + E) log V) with Fibonacci Heap")
print("Space Complexity: O(V^2 + E)")