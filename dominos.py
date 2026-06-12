
# m , n = map(int , input().split())
# print((m*n)//2)
adj = {
    0: [1, 2],
    1: [2]
}
n=len(adj)
visited=[False]*(n+1)
def dfs(u , visited , adj):
    if visited[u]:
        return
    visited[u]=True
    print(u)
    for v in adj[u]:
        if not visited[v]:
            dfs(v , visited , adj)
dfs(0 , visited , adj)