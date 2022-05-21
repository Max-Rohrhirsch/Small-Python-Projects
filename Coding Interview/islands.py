def solve(grid):
    if grid == None or len(grid) == 0:
        return 0

    numIslands = 0
    for idx, val in enumerate(grid):
        for idx2, val2 in enumerate(grid[0]):
            if val2 == '1':
                numIslands += 
