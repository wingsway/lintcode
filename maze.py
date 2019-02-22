DIRECTIONS = [(1, 0), (-1, 0), (0, -1), (0, 1)]
class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if not maze:
            return False
        visited, self.ans = set([(start[0], start[1])]), False
        self.dfs_helper(maze, start[0], start[1], destination, visited)
        return self.ans

    def dfs_helper(self, maze, x, y, destination, visited):
        if self.ans or self.is_des(x, y, destination):
            self.ans = True
            return
        for dx, dy in DIRECTIONS:
            new_x, new_y = x, y
            while self.is_valid(maze, new_x+dx, new_y+dy):
                new_x += dx
                new_y += dy
            coor = (new_x, new_y)
            if coor not in visited:
                visited.add(coor)
                self.dfs_helper(maze, new_x, new_y, destination, visited)

    def is_valid(self, maze, x, y):
        row, col = len(maze), len(maze[0])
        return x >= 0 and x < row and y >= 0 and y < col and maze[x][y] == 0

    def is_des(self, x, y, destination):
        return x == destination[0] and y == destination[1]
