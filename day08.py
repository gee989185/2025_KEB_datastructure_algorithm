def dfs(g, i, visited):
    visited[i] = 1
    print(chr(ord('A')+i), end=' ')
    for j in range(len(g)):
        if g[i][j] == 1 and not visited[j]:     # 연결이 되어 있으면서 / 동시에 방문한 적이 없는

            dfs(g, j, visited)

graph = [
    [0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

visited = [0] * len(graph)
dfs(graph, 0, visited)
# if g[i][j] == "1" and not visited[j]
# i = 0: A C B D E
# i = 1: B C A D E
# i = 2: C A D B E
# i = 3: D A C B E
# i = 4: E C A D B

# if g[i][j] == "0" and not visited[j]
# i = 0: A B D E
# i = 1: B A E D
# i = 2: C
# i = 3: D B A E