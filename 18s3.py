from collections import deque

# Directions for up, down, left, right
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
conveyor_directions = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

def bfs_from_start(grid, N, M, start):
    # BFS to calculate minimum steps from the start
    dist = [[-1] * M for _ in range(N)]
    dist[start[0]][start[1]] = 0
       #Check if robot is captured at start by cameras
    if grid[start[0]][start[1]] == 'X':
        grid[start[0]][start[1]] = 'S'        
        return dist
    queue = deque([start])
    
    while queue:
        x, y = queue.popleft()
        
        # If we're on a conveyor, move automatically in its direction
        if grid[x][y] in conveyor_directions:
            dx, dy = conveyor_directions[grid[x][y]]
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != 'W' and grid[nx][ny] != 'X' and dist[nx][ny] == -1 or dist[nx][ny] > dist[x][y] + 1:
                dist[nx][ny] = dist[x][y]
                queue.append((nx, ny))
                
        else:
        # Try moving in all 4 directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != 'W' :
                
                    if grid[nx][ny] == '.' or  grid[nx][ny] in conveyor_directions:
                        if dist[nx][ny] == -1 or dist[nx][ny] > dist[x][y] + 1:
                            dist[nx][ny] = dist[x][y] + 1
                            queue.append((nx, ny))
            
        
    
    return dist

def dfs_from_cameras(grid, N, M):
    # dFS to mark cells visible to cameras
   
    queue = deque()
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'C':
                queue.append((i, j))
              
    while queue:
        x, y = queue.popleft()
        
        # Spread camera vision in all 4 directions
        for dx, dy in directions:
            nx, ny = x, y
            while True:
                nx += dx
                ny += dy
                if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] != 'W' and grid[nx][ny] != 'C':
                    if grid[nx][ny] == '.' or grid[nx][ny] == 'S':
                        grid[nx][ny] = 'X'
                else:
                    break
    
    return 

def solve(N, M, grid):
    # Find start position
    start = None
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 'S':
                start = (i, j)
                break
    
    # Mark the cells visible by cameras
    dfs_from_cameras(grid, N, M)
 
    # Perform BFS from the start to calculate the minimum steps
    dist = bfs_from_start(grid, N, M, start)
    
    # Output results for all empty cells
    for i in range(N):
        for j in range(M):
            if grid[i][j] == '.' or grid[i][j] == 'X' :
                if dist[i][j] != -1: #and not visible[i][j]:
                    print(dist[i][j])
                else:
                    print(-1)
            elif grid[i][j] == 'S':
                continue
            else:
                continue

# Input reading
N, M = map(int, input().split())


in_grid = [input().strip() for _ in range(N)]
grid = [list(s) for s in in_grid]

# Solve the problem
solve(N, M, grid)