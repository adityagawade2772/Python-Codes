class Solution:
    def dfs(self, node,visited,nodecount,stack,adj):
        visited[node]=1
        for adjnode in adj[node]:
            if visited[adjnode] ==0:
                self.dfs(adjnode,visited,nodecount,stack,adj)
        stack.append(node)
    def topoSort(self, adj: list[list[int]]) -> list[int]:
        # code here
    
        nodecount= len(adj)
        visited=[0]*nodecount
        stack = []
        for i in range(nodecount):
            if visited[i]==0:
                self.dfs(i,visited,nodecount,stack,adj)
        return stack[::-1]