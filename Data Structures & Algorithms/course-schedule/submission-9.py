class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqCount = defaultdict(int)
        dep = defaultdict(list)
        process = []
        fin = 0
        for course,preq in prerequisites:
            preqCount[course] += 1
            dep[preq].append(course)
        for i in range(numCourses):
            if preqCount[i] == 0:
                fin+= 1
                process.append(i)
        print(process)
        print(dep)
        print(preqCount)
        while fin != numCourses:
            if not process:
                return False
            proc = process.pop()
            for course in dep[proc]:
                preqCount[course] -= 1
                if preqCount[course] == 0:
                    process.append(course)
                    fin+=1

        return True

        