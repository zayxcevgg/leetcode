class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        magicSquares = 0
        height = len(grid)
        width = len(grid[0])
        for iterVert in range(0, height-2):
            for iterHor in range(0, width-2):
                print(grid[iterVert][iterHor:iterHor+3])
                print(grid[iterVert+1][iterHor:iterHor+3])
                print(grid[iterVert+2][iterHor:iterHor+3])

                row1 = grid[iterVert][iterHor:iterHor+3]
                row2 = grid[iterVert+1][iterHor:iterHor+3]
                row3 = grid[iterVert+2][iterHor:iterHor+3]

                magicSquares += self.uniqueCheck(row1, row2, row3)
        print(magicSquares)
        return magicSquares

    def uniqueCheck(self, row1, row2, row3):

        uniquenessCheck = []
        vert1 = row1[0] + row2[0] + row3[0]
        vert2 = row1[1] + row2[1] + row3[1]
        vert3 = row1[2] + row2[2] + row3[2]
        diag1 = row1[0] + row2[1] + row3[2]
        diag2 = row1[2] + row2[1] + row3[0]
        # sums check
        if sum(row1) == sum(row2) == sum(row3) == vert1 == vert2 == vert3 == diag1 == diag2:        
            pass
        else:
            return 0
        
        for row in row1, row2, row3:
                for element in row:
                    # only 1 to 9 nums check
                    if element > 0 and element < 10:
                        uniquenessCheck.append(element)
                    else:
                        break
                    
        # check for uniqueness
        if len(uniquenessCheck) == len(set(uniquenessCheck)) == 9:
            return 1
        else:
            return 0

        
    



obj = Solution()
grid = [[1,8,6],[10,5,0],[4,2,9]]
obj.numMagicSquaresInside(grid)