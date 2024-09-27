class Solution:
    def getTotalIsles(self, grid):
        if not grid:
            return 0
        
        # Define the number of rows and columns
        rows = len(grid)
        cols = len(grid[0])

        # This will be used to mark cells that are part of an island
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        
        # Directions for moving in the grid: Up, Down, Left, Right
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        # Depth-First Search to explore the island
        def dfs(r, c):
            visited[r][c] = True
            # Explore all 4 possible directions
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                # Check if new position is within bounds and not visited and is land
                if 0 <= new_r < rows and 0 <= new_c < cols and not visited[new_r][new_c] and grid[new_r][new_c] == 'L':
                    dfs(new_r, new_c)
        
        # Number of islands
        num_islands = 0
        
        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):
                # If we find an unvisited land cell, we initiate a DFS, which means a new island
                if grid[r][c] == 'L' and not visited[r][c]:
                    num_islands += 1
                    dfs(r, c)
        
        return num_islands
