class Solution:
    def solve(self, node,adj, visited, result):
        visited[node] = 1
        result.append(node)
        for i in adj[node]:
            if visited[i] ==0:
                self.solve(i,adj,visited,result)
                
        
    def dfs(self, adj):
        # code here
        n = len(adj)
        visited = [0]*n
        result = []
        self.solve(0,adj,visited,result)
        return result
        
        