from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islandCount = 0
        visited = set()
        def bfsTraversal(row, col):
            curQueue = deque()
            curQueue.append((row, col))
            while curQueue:
                #print("Queue still active!")
                curCoord = curQueue.popleft()
                row = curCoord[0]
                col = curCoord[1]
                visited.add((row, col))
                if col+1 in range(0, len(grid[row])) and grid[row][col+1] == "1":
                    if (row, col+1) not in visited:
                        curQueue.append((row, col+1))
                if  col-1 in range(0, len(grid[row])) and grid[row][col-1] == "1":
                    if (row, col-1) not in visited:
                        curQueue.append((row, col-1))
                if row+1 in range(0, len(grid)) and grid[row+1][col] == "1":
                    if (row+1, col) not in visited:
                        curQueue.append((row+1, col))
                if row-1 in range(0, len(grid)) and grid[row-1][col] == "1":
                    if (row-1, col) not in visited:
                        curQueue.append((row-1, col))
                #print(f"Queue: {curQueue}")
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                if grid[i][j] == "1" and (i, j) not in visited:
                    bfsTraversal(i, j)
                    islandCount += 1
                    #print(f"Visited: {visited}")
        return islandCount


