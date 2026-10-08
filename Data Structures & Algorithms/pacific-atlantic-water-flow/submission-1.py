from collections import deque
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                pac = 0
                atl = 0
                visited = set()
                queue = deque()
                queue.append((r,c))
                while queue:
                    r_curr, c_curr = queue.popleft()
                    if r_curr == 0 or c_curr == 0:
                        pac += 1
                    if r_curr == len(heights)-1 or c_curr == len(heights[0])-1:
                        atl += 1
                    if pac and atl:
                        res.append([r,c])
                        break
                    if r_curr > 0 and (r_curr-1,c_curr) not in visited and heights[r_curr][c_curr] >= heights[r_curr-1][c_curr]:
                        queue.append((r_curr-1,c_curr))
                        visited.add((r_curr-1,c_curr))
                    if r_curr < len(heights)-1 and (r_curr+1,c_curr) not in visited and heights[r_curr][c_curr] >= heights[r_curr+1][c_curr]:  
                        queue.append((r_curr+1,c_curr))
                        visited.add((r_curr+1,c_curr))
                    if c_curr > 0 and (r_curr,c_curr-1) not in visited and  heights[r_curr][c_curr] >= heights[r_curr][c_curr-1]: 
                        queue.append((r_curr,c_curr-1))
                        visited.add((r_curr,c_curr-1))
                    if c_curr < len(heights[0])-1 and (r_curr,c_curr+1) not in visited and heights[r_curr][c_curr] >= heights[r_curr][c_curr+1]: 
                        queue.append((r_curr,c_curr+1))
                        visited.add((r_curr,c_curr+1))
        return res
                        
            
            
            

