class Solution:
    def createGrid(self, m: int, n: int) -> List[str]:
        # Initialize the grid with obstacles ('#')
        res = [['#' for _ in range(n)] for _ in range(m)]
        
        # Make the first row all free cells ('.')
        for j in range(n):
            res[0][j] = '.'
            
        # Make the last column all free cells ('.')
        for i in range(m):
            res[i][n - 1] = '.'
            
        return ["".join(row) for row in res]