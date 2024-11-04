import heapq  # For priority queue usage
import random  # For generating random resources and needs

class Graph:
    def __init__(self):
        # Initialize an empty graph with dictionaries for resources, needs, and population
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

        print('Resources before distribution: {}'.format(self.resources))  # Changed to .format()
        print('Needs before distribution: {}'.format(self.needs))  # Changed to .format()

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
                    print('Distributing {} resources from {} to {}'.format(amount_to_distribute, source, island))  # Changed to .format()

        # Print distribution results
        print("\n--- Distribution Results ---")
        print("Resources remaining after distribution:")
        for island in sorted(self.resources):
            print("  {}: {}".format(island, self.resources[island]))  # Changed to .format()
        print("Needs after distribution:")
        for island in sorted(self.needs):
            print("  {}: {}".format(island, self.needs[island]))  # Changed to .format()
        print("Total resources distributed:")
        for island in sorted(distributed_resources):
            print("  {}: {}".format(island, distributed_resources[island]))  # Changed to .format()

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
        islands_by_priority = sorted(self.graph.keys(),
                                     key=lambda x: (-self.population.get(x, 0), dist[x]))

        # Output the skill-sharing schedule
        print("\n--- Skill-Sharing Schedule ---")
        for island in islands_by_priority:
            print('  Island: {}, Travel Time: {}'.format(island, dist[island]))  # Changed to .format()

# Example usage
if __name__ == "__main__":
    graph = Graph()

    # Generate random resources and needs for the islands
    resources_A = random.randint(10, 20)  # Random resources for Island A
    needs_B = random.randint(5, 15)  # Random needs for Island B
    needs_C = random.randint(1, 10)  # Random needs for Island C
    needs_D = random.randint(1, 10)  # Random needs for Island D

    # Add edges (connections) between the islands
    graph.add_edge('IslandA', 'IslandB', 2)
    graph.add_edge('IslandA', 'IslandC', 3)
    graph.add_edge('IslandA', 'IslandD', 3)

    # Set initial resources, needs, and population
    graph.set_resources('IslandA', resources_A)
    graph.set_needs('IslandB', needs_B)
    graph.set_needs('IslandC', needs_C)
    graph.set_needs('IslandD', needs_D)
    graph.set_population('IslandB', 300)
    graph.set_population('IslandC', 200)
    graph.set_population('IslandD', 400)

    # Execute resource distribution
    distributed_resources = graph.dijkstra_and_distribute('IslandA')

    # Generate a skill-sharing schedule
    graph.schedule_skill_sharing('IslandA')
