from collections import deque

class Solution:
    def isCycle(self, adj: list) -> bool:

        v = len(adj)
        visited = [0] * v
        queue = deque()

        for start in range(v):

            if visited[start] == 1:
                continue

            visited[start] = 1
            queue.append((start, -1))

            while queue:
                node, parent = queue.popleft()

                for adjnode in adj[node]:

                    if visited[adjnode] == 0:
                        visited[adjnode] = 1
                        queue.append((adjnode, node))

                    elif adjnode != parent:
                        return True

        return False