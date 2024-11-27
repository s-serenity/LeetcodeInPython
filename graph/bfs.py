import collections
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])
        def bfs(maze,entrance):
            q = collections.deque()
            q.append((entrance[0], entrance[1], 0))  # (x, y, steps)
            maze[entrance[0]][entrance[1]] = '+'  # 标记入口为已访问

            while q:
                x, y, steps = q.popleft()

                # 四个方向的邻居
                neighbors = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]

                for nx, ny in neighbors:
                    if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                        if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                            return steps + 1  # 找到出口
                        maze[nx][ny] = '+'  # 标记为已访问
                        q.append((nx, ny, steps + 1))

            return -1
        return bfs(maze,entrance)

    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        entrances = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    entrances.append([i, j])

        def bfs(grid, entrances):
            q = collections.deque()
            steps_set = []
            for entrance in entrances:
                q.append((entrance[0], entrance[1], 0))  # (x, y, steps)
                grid[entrance[0]][entrance[1]] = 2  # 标记入口为已访问
            while q:
                x, y, steps = q.popleft()
                steps_set.append(steps)

                # 四个方向的邻居
                neighbors = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
                for nx, ny in neighbors:
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        q.append((nx, ny, steps + 1))
            return steps_set

        steps_set = bfs(grid, entrances)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        if len(steps_set) > 0:
            return steps_set[-1]
        else:
            return 0


maze = [[".","+"]]
entrance = [0,0]
Solution().nearestExit(maze,entrance)