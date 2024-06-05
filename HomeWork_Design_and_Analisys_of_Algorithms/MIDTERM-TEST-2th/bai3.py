def dfs(u, graph, visited, path):
  visited[u] = True
  for v in graph[u]:
    if not visited[v]:
      path.append((u, v))
      if dfs(v, graph, visited, path):
        return True
    elif (v, u) not in path:
      return True  # Phát hiện chu trình
  return False

def main():
  
  with open("DATA.IN", "r") as f:
          N = int(f.readline())
          graph = [[] for _ in range(N)]
          for i in range(N):
              row = f.readline().split() 
              for j, val in enumerate(row):
                  if int(val) == 1:
                      graph[i].append(j)


  visited = [False] * N
  path = []
  has_cycle = False
  for i in range(N):
    if not visited[i]:
      if dfs(i, graph, visited, path):
        has_cycle = True
        break

  with open("DATA.OUT", "w", encoding="utf-8") as f:
    if not has_cycle:
      f.write(f"{len(path)}\n")
      for u, v in path:
        f.write(f"{u + 1} {v + 1}\n")  # Đánh số nút từ 1
    else:
      f.write("Vô nghiệm\n")

if __name__ == "__main__":
  main()
