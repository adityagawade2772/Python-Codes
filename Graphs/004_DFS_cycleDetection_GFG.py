class Solution:

    def dfs(self, node, parent, visited, adj):

        visited[node] = 1

        for adjnode in adj[node]:

            if visited[adjnode] == 0:

                a = self.dfs(adjnode, node, visited, adj)

                if a:
                    return True

            elif adjnode != parent:
                return True

        return False

    def isCycle(self, adj: list) -> bool:

        v = len(adj)
        visited = [0] * v

        for i in range(v):

            if visited[i] == 0:

                if self.dfs(i, -1, visited, adj):
                    return True

        return False