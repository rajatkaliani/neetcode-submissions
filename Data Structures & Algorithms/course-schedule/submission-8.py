class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # preq[i] = [a,b]
        # take B to take A

        indegree = defaultdict(int)
        courses = defaultdict(list)
        for i in range(numCourses):
            indegree[i] = 0
        for course,prereq in prerequisites:
            indegree[course] += 1
            courses[prereq].append(course)

        fin = []
        queue = []
        for course,count in indegree.items():
            if count == 0:
                queue.append(course)
                fin.append(course)
        while queue:
            proc = queue.pop()
            for c in courses[proc]:
                indegree[c] -= 1
                if indegree[c] == 0:
                    queue.append(c)
                    fin.append(c)
        return len(fin) == numCourses

            
        
