import heapq
from typing import List


class Solution:
    def shortestPath(
        self,
        n: int,
        edges: List[List[int]],
        labels: str,
        k: int
    ) -> int:
        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        width = k + 1
        INF = 10**18
        dist = [INF] * (n * width)

        dist[1] = 0
        heap = [(0, 0, 1)]

        while heap:
            cost, u, run = heapq.heappop(heap)

            index = u * width + run
            if cost != dist[index]:
                continue

            for v, weight in graph[u]:
                next_run = run + 1 if labels[u] == labels[v] else 1

                if next_run > k:
                    continue

                next_cost = cost + weight
                next_index = v * width + next_run

                if next_cost < dist[next_index]:
                    dist[next_index] = next_cost
                    heapq.heappush(
                        heap,
                        (next_cost, v, next_run)
                    )

        target = (n - 1) * width
        answer = min(dist[target + run] for run in range(1, k + 1))

        return -1 if answer == INF else answer