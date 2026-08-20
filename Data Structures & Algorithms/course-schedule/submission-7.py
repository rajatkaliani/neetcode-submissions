class Solution:
    from collections import deque
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        preqList = defaultdict(int)
        for c,p in prerequisites:
            adjList[p].append(c)
            preqList[c] += 1
        proc = deque()
        for num in range(numCourses):
            if preqList[num] == 0:
                proc.append(num)
        fin = 0
        while proc:
            procNum = proc.popleft()
            fin += 1
            for rem in adjList[procNum]:
                preqList[rem] -= 1
                if preqList[rem] == 0:
                    proc.append(rem)
            
        return fin == numCourses


