class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        req_map = {
            i: [] for i in range(numCourses)
        }

        for course, prereq in prerequisites:
            req_map[course].append(prereq)
        
        output = []
        visited, cycle = set(), set()

        def dfs(course):
            if course in cycle:
                return False

            if course in visited:
                return True  

            cycle.add(course)
            
            for pre in req_map[course]:
                if not dfs(pre):
                    return False 
            
            cycle.remove(course)

            # Adding the confirmed good node after ensuring that it's not part of a cycle.
            visited.add(course)
            output.append(course)
            return True 
        
        for course in range(numCourses):
            if not dfs(course):
                return []
        
        return output 

print(Solution().findOrder(numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]))