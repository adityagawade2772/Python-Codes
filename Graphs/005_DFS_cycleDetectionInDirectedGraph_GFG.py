class Solution:
    def dfs(self,node,visited,path,adj):
        path[node]=1
        visited[node]= 1
        for adjnode in adj[node]:
            if visited[adjnode]==0:
                x =self.dfs(adjnode,visited,path,adj)
                if x ==True:
                    return True
            elif path[adjnode]==1:
                return True
        path[node]=0
        return False
    def isCyclic(self, adj: list[list[int]]) -> bool:
        # code here
        nodecount= len(adj)
        visited = [0]*nodecount
        path = [0]*nodecount
        for i in range(nodecount):
            if visited[i]==0:
                a=self.dfs(i,visited,path,adj)
                if a== True:
                    return True
        return False 