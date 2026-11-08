class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        M,N=len(grid),len(grid[0])
        for i in range(M):
            row_sum=sum(grid[i])
            if row_sum >1:
                for j in range(N):
                    if grid[i][j]==1:
                        grid[i][j]=-1
        for j in range(N):
            col_sum=0
            for i in range(M):
                if grid[i][j]!=0:
                    col_sum+=1
            if col_sum>1:
                for i in range(M):
                    if grid[i][j]==1:
                        grid[i][j]=-1
        count=0
        for i in range(M):
            for j in range(N):
                if grid[i][j]==-1:
                    count+=1
        return count


        