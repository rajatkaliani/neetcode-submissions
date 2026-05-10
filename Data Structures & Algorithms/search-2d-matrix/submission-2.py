class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rl = 0 # row left
        rr = len(matrix) - 1 # row right
        while (rl < rr):
            midr = (rl + rr) // 2
            if matrix[midr][len(matrix[0]) - 1] < target:
                rl = midr + 1
            else:
                rr = midr
        cl = 0
        cr = len(matrix[0]) - 1
        while (cl < cr):
            midc = (cl + cr) // 2
            if matrix[rl][midc] < target:
                cl = midc +1
            else:
                cr = midc
        if matrix[rl][cl] == target:
            return True
        return False

            
            
                
            
        


