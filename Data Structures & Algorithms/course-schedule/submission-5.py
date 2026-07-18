class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        fin = []
        # preq:[list of courses dependant on preq]
        adjList = defaultdict(list)
        count = defaultdict(int)
        for p,c in prerequisites:
            adjList[c].append(p)
            count[p] += 1
        while len(fin) != numCourses:
            ctr = 0
            for num in range(numCourses):
                if count[num] == 0:
                    fin.append(num)
                    for elm in adjList[num]:
                        count[elm] -= 1
                    count[num] -= 1    
                    ctr += 1
            print(fin)
            if ctr == 0:
                return False
        return True     
                
                
            
        
