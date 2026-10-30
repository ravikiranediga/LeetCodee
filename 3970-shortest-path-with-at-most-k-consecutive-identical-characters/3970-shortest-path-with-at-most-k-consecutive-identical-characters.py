import heapq

class Solution:
    def shortestPath(self, n, edges, labels, k):

        # Step 1: Build adjacency list
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        # Required input storage
        mavorqeli = (n, edges, labels, k)

        # Step 2: Create distance array
        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        # Step 3: Initialize starting state
        dist[0][1] = 0

        # (cost, node, consecutive_count)
        heap = [(0, 0, 1)]

        # Step 4: Dijkstra algorithm
        while heap:

            cost, u, count = heapq.heappop(heap)

            # Skip outdated states
            if cost > dist[u][count]:
                continue

            # Destination reached
            if u == n - 1:
                return cost

            # Step 5: Visit neighboring nodes
            for v, weight in graph[u]:

                # Calculate next consecutive count
                if labels[u] == labels[v]:
                    new_count = count + 1
                else:
                    new_count = 1

                # Reject invalid paths
                if new_count > k:
                    continue

                new_cost = cost + weight

                # Update if a cheaper path is found
                if new_cost < dist[v][new_count]:

                    dist[v][new_count] = new_cost

                    heapq.heappush(
                        heap,
                        (new_cost, v, new_count)
                    )

        # No valid path exists
        return -1