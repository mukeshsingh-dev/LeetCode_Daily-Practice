from typing import List


class Solution:
    def palindromePath(
        self,
        n: int,
        edges: List[List[int]],
        s: str,
        queries: List[str]
    ) -> List[bool]:

        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        node_mask = [1 << (ord(ch) - ord("a")) for ch in s]

        # Tree information
        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        tout = [0] * n
        initial_prefix = [0] * n

        # Iterative DFS to avoid Python recursion limits.
        timer = 0
        stack = [(0, -1, False)]

        while stack:
            node, par, exiting = stack.pop()

            if not exiting:
                parent[node] = node if par == -1 else par
                depth[node] = 0 if par == -1 else depth[par] + 1

                previous = 0 if par == -1 else initial_prefix[par]
                initial_prefix[node] = previous ^ node_mask[node]

                tin[node] = timer
                timer += 1

                stack.append((node, par, True))

                for neighbor in reversed(graph[node]):
                    if neighbor != par:
                        stack.append((neighbor, node, False))
            else:
                tout[node] = timer - 1

        # Binary lifting table for LCA.
        levels = max(1, n.bit_length())
        up = [parent[:]]

        for level in range(1, levels):
            previous = up[level - 1]
            current = [0] * n

            for node in range(n):
                current[node] = previous[previous[node]]

            up.append(current)

        def lca(u: int, v: int) -> int:
            if depth[u] < depth[v]:
                u, v = v, u

            difference = depth[u] - depth[v]
            bit = 0

            while difference:
                if difference & 1:
                    u = up[bit][u]
                difference >>= 1
                bit += 1

            if u == v:
                return u

            for level in range(levels - 1, -1, -1):
                if up[level][u] != up[level][v]:
                    u = up[level][u]
                    v = up[level][v]

            return parent[u]

        # Fenwick tree supporting subtree XOR updates and point queries.
        fenwick = [0] * (n + 2)

        def fenwick_update(index: int, value: int) -> None:
            index += 1

            while index < len(fenwick):
                fenwick[index] ^= value
                index += index & -index

        def range_xor(left: int, right: int, value: int) -> None:
            fenwick_update(left, value)
            fenwick_update(right + 1, value)

        def point_xor(index: int) -> int:
            result = 0
            index += 1

            while index > 0:
                result ^= fenwick[index]
                index -= index & -index

            return result

        def current_prefix(node: int) -> int:
            return initial_prefix[node] ^ point_xor(tin[node])

        answer = []

        for query in queries:
            parts = query.split()

            if parts[0] == "update":
                node = int(parts[1])
                new_character = parts[2]
                new_mask = 1 << (ord(new_character) - ord("a"))

                difference = node_mask[node] ^ new_mask

                if difference:
                    node_mask[node] = new_mask

                    # Changing this node changes the root-prefix mask of every
                    # node in its subtree.
                    range_xor(tin[node], tout[node], difference)

            else:
                u = int(parts[1])
                v = int(parts[2])
                ancestor = lca(u, v)

                path_mask = (
                    current_prefix(u)
                    ^ current_prefix(v)
                    ^ node_mask[ancestor]
                )

                # A string can be rearranged into a palindrome when at most
                # one character has an odd frequency.
                answer.append(
                    path_mask == 0
                    or (path_mask & (path_mask - 1)) == 0
                )

        return answer