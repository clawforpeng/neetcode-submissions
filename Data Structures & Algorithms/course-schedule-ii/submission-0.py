class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereqMap = {}
        sols = []
        visited = set()
        complete = set()

        for prerequisite in prerequisites:
            course = prerequisite[0]
            p = prerequisite[1]

            if course in prereqMap:
                prereqMap[course].append(p)
            else:
                prereqMap[course] = [p]
        
        def dfs(course: int) -> bool:
            # if course not in prereqMap:
            #     return [course]
            
            if course in visited:
                return False
            
            if course in complete:
                return True

            visited.add(course)
            
            for prereq in prereqMap.get(course, []):
                if not dfs(prereq):
                    return False

            visited.remove(course)
            complete.add(course)

            sols.append(course)
            return True
        
        for i in range(numCourses):
            sol = dfs(i)
            if not sol:
                return []
        
        return sols