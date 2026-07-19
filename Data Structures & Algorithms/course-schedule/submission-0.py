class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        ans = True

        for prerequisite in prerequisites:
            prereq = prerequisite[1]
            course = prerequisite[0]
            
            if not course in adjList:
                adjList[course] = [prereq]
            else:
                adjList[course].append(prereq)

        def detectCycle(visited: Set[int], course: int) -> bool:
            if course in visited:
                return False
            
            if course not in adjList:
                return True
            
            sol = True
            visited.add(course)
            for prereq in adjList[course]:
                sol = sol and detectCycle(visited, prereq)
                if not sol:
                    return False
            
            visited.remove(course)

            return sol
            
        
        for i in range(numCourses):
            if i in adjList:
                for j in adjList[i]:
                    visited = set()
                    visited.add(i)
                    ans = ans and detectCycle(visited, j)

                    if not ans:
                        return False
        
        return ans
        
        
        