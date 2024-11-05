import heapq

class Graph:

    # Task 3 Implementation (Ralph Ramos) ############################################################################################################
    def __init__(self):
        self.graph = {}
        self.resources = {}
        self.needs = {}
    
    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:  # Ensure the neighbor is also added
            self.graph[v] = []
        self.graph[u].append((v, weight))
    
    def set_resources(self, island, quantity):
        self.resources[island] = quantity
    
    def set_needs(self, island, quantity):
        self.needs[island] = quantity
    
    def dijkstra_and_distribute(self, source):
        # Step 1: Run Dijkstra's algorithm to find shortest paths
        dist = {island: float('inf') for island in self.graph}
        dist[source] = 0
        priority_queue = [(0, source)]  # (distance, island)

        print(f'Resources before distribution: {self.resources}')
        print(f'Needs before distribution: {self.needs}')

        while priority_queue:
            current_distance, current_island = heapq.heappop(priority_queue)

            # Step 2: Explore neighbors
            for neighbor, travel_time in self.graph.get(current_island, []):
                alt = current_distance + travel_time
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    heapq.heappush(priority_queue, (alt, neighbor))

        # Step 3: Distribute resources based on needs
        distributed_resources = {island: 0 for island in self.graph}
        for island in sorted(dist.keys(), key=dist.get):  # Process by increasing distance
            if self.resources.get(source, 0) > 0:  # Only distribute from the source
                while self.resources[source] > 0 and self.needs.get(island, 0) > 0:
                    amount_to_distribute = min(self.resources[source], self.needs[island])
                    self.resources[source] -= amount_to_distribute
                    self.needs[island] -= amount_to_distribute
                    distributed_resources[island] += amount_to_distribute

        return distributed_resources

        # Task 3 End (Ralph Ramos) ############################################################################################################
        

# Task 3 Example usage (Ralph Ramos)############################################################################################################
graph = Graph()
graph.add_edge('IslandA', 'IslandB', 2)
graph.add_edge('IslandA', 'IslandC', 3)
graph.add_edge('IslandB', 'IslandD', 1)

# Set initial resources and needs
graph.set_resources('IslandA', 10)
graph.set_needs('IslandB', 5)
graph.set_needs('IslandC', 3)
graph.set_needs('IslandD', 2)

# Execute resource distribution
distributed_resources = graph.dijkstra_and_distribute('IslandA')

# Output results
print(f'Resources remaining After Distribution: {graph.resources}')
print(f'Needs after distribution: {graph.needs}')
print(f'Total resources distributed after distribution: {distributed_resources}')

