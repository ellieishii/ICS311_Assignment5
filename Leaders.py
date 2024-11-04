import heapq # For Priority Queue usage

class Graph:
    def __init__(self):
        # Initialize an empty graph with dictionaries for resources, needs, and population.
        self.graph = {}
        self.resources = {}
        self.needs = {}
        self.population = {}

    def add_edge(self, u, v, weight):
        # Add directed edge from island `u` to `v` with travel time `weight`
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:  # Ensure the neighbor is also added
            self.graph[v] = []
        self.graph[u].append((v, weight))

    def set_resources(self, island, quantity):
        # Set the available resources at a specific island
        self.resources[island] = quantity

    def set_needs(self, island, quantity):
        # Set the needed resources at a specific island
        self.needs[island] = quantity

    def set_population(self, island, population):
        # Set the population of a specific island for prioritizing skill-sharing
        self.population[island] = population

    def dijkstra_and_distribute(self, source):
        # Step 1: Run Dijkstra's algorithm to find shortest paths
        dist = {island: float('inf') for island in self.graph}
        dist[source] = 0
        priority_queue = [(0, source)]  # (distance, island), initialize priority queue

        print(f'Resources before distribution: {self.resources}')
        print(f'Needs before distribution: {self.needs}')

        # Execute Dijkstra's algorithm
        while priority_queue:
            current_distance, current_island = heapq.heappop(priority_queue)

            # Explore neighbors
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

        # Return the amount of resources distributed to each island
        return distributed_resources

    def schedule_skill_sharing(self, source):
        # Step 1: Calculate shortest paths from the source using Dijkstra's algorithm
        dist = {island: float('inf') for island in self.graph}
        dist[source] = 0
        priority_queue = [(0, source)]  # (distance, island)

        while priority_queue:
            current_distance, current_island = heapq.heappop(priority_queue)

            # Explore neighbors
            for neighbor, travel_time in self.graph.get(current_island, []):
                alt = current_distance + travel_time
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    heapq.heappush(priority_queue, (alt, neighbor))

        # Step 2: Prioritize islands for skill-sharing based on population and distance
        # Sorting by population in descending order, then by distance in ascending order
        islands_by_priority = sorted(self.graph.keys(),
                                     key=lambda x: (-self.population.get(x, 0), dist[x]))

        # Output the skill-sharing schedule
        schedule = [(island, dist[island]) for island in islands_by_priority]
        return schedule

# Example usage
graph = Graph()
graph.add_edge('IslandA', 'IslandB', 2)
graph.add_edge('IslandA', 'IslandC', 3)
graph.add_edge('IslandB', 'IslandD', 1)
graph.add_edge('IslandC', 'IslandD', 4)

# Set initial resources, needs, and population
graph.set_resources('IslandA', 10)
graph.set_needs('IslandB', 5)
graph.set_needs('IslandC', 3)
graph.set_needs('IslandD', 2)
graph.set_population('IslandB', 300)
graph.set_population('IslandC', 200)
graph.set_population('IslandD', 400)

# Execute resource distribution
distributed_resources = graph.dijkstra_and_distribute('IslandA')

# Output results of distribution
print(f'Resources remaining after distribution: {graph.resources}')
print(f'Needs after distribution: {graph.needs}')
print(f'Total resources distributed: {distributed_resources}')

# Generate a skill-sharing schedule
skill_sharing_schedule = graph.schedule_skill_sharing('IslandA')
print("Skill-sharing schedule (island, travel time):", skill_sharing_schedule)import heapq  # For Priority Queue usage

class Graph:
    def __init__(self):
        # Initialize an empty graph with dictionaries for resources, needs, and population.
        self.graph = {}
        self.resources = {}
        self.needs = {}
        self.population = {}

    def add_edge(self, u, v, weight):
        # Add directed edge from island `u` to `v` with travel time `weight`
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:  # Ensure the neighbor is also added
            self.graph[v] = []
        self.graph[u].append((v, weight))

    def set_resources(self, island, quantity):
        # Set the available resources at a specific island
        self.resources[island] = quantity

    def set_needs(self, island, quantity):
        # Set the needed resources at a specific island
        self.needs[island] = quantity

    def set_population(self, island, population):
        # Set the population of a specific island for prioritizing skill-sharing
        self.population[island] = population

    def dijkstra_and_distribute(self, source):
        # Step 1: Run Dijkstra's algorithm to find shortest paths
        dist = {island: float('inf') for island in self.graph}
        dist[source] = 0
        priority_queue = [(0, source)]  # (distance, island), initialize priority queue

        print(f'Resources before distribution: {self.resources}')
        print(f'Needs before distribution: {self.needs}')

        # Execute Dijkstra's algorithm
        while priority_queue:
            current_distance, current_island = heapq.heappop(priority_queue)

            # Explore neighbors
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

        # Return the amount of resources distributed to each island
        return distributed_resources

    def schedule_skill_sharing(self, source):
        # Step 1: Calculate shortest paths from the source using Dijkstra's algorithm
        dist = {island: float('inf') for island in self.graph}
        dist[source] = 0
        priority_queue = [(0, source)]  # (distance, island)

        while priority_queue:
            current_distance, current_island = heapq.heappop(priority_queue)

            # Explore neighbors
            for neighbor, travel_time in self.graph.get(current_island, []):
                alt = current_distance + travel_time
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    heapq.heappush(priority_queue, (alt, neighbor))

        # Step 2: Prioritize islands for skill-sharing based on population and distance
        # Sorting by population in descending order, then by distance in ascending order
        islands_by_priority = sorted(self.graph.keys(),
                                     key=lambda x: (-self.population.get(x, 0), dist[x]))

        # Output the skill-sharing schedule
        schedule = [(island, dist[island]) for island in islands_by_priority]
        return schedule

# Example usage
graph = Graph()
graph.add_edge('IslandA', 'IslandB', 2)
graph.add_edge('IslandA', 'IslandC', 3)
graph.add_edge('IslandB', 'IslandD', 1)
graph.add_edge('IslandC', 'IslandD', 4)

# Set initial resources, needs, and population
graph.set_resources('IslandA', 10)
graph.set_needs('IslandB', 5)
graph.set_needs('IslandC', 3)
graph.set_needs('IslandD', 2)
graph.set_population('IslandB', 300)
graph.set_population('IslandC', 200)
graph.set_population('IslandD', 400)

# Execute resource distribution
distributed_resources = graph.dijkstra_and_distribute('IslandA')

# Output results of distribution
print(f'Resources remaining after distribution: {graph.resources}')
print(f'Needs after distribution: {graph.needs}')
print(f'Total resources distributed: {distributed_resources}')

# Generate a skill-sharing schedule
skill_sharing_schedule = graph.schedule_skill_sharing('IslandA')
print("Skill-sharing schedule (island, travel time):", skill_sharing_schedule)
