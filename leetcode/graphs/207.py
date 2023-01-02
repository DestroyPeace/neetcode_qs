class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        req_map = {
            i: [] for i in range(numCourses)
        }
    
        # Creating our hash map:
        for a, b in prerequisites:
            req_map[a].append(b)

        visited = set()

        def dfs(course):
            """
            We're visiting a course twice - therefore a loop exists and therefore
            you cannot complete the courses due to one pair requiring each other as a
            prerequisite.
            """
            
            # Checking for cycles by checking if the node has been previously checked.
            if course in visited: 
                return False 

            # That means we've finally iterated until we found a course that doesn't 
            # require any prerequisites, meaning that you can complete them all.
            if req_map[course] == []:
                return True 

            # Adding the course to visited to ensure that no cycle exists in the base check.
            visited.add(course)
            
            for pre in req_map[course]:
                # If the course is unable to be visited, e.g due to already visiting,
                # then we return False.
                if not dfs(pre): 
                    return False 

            # Removing the course as we now know there exists no cycles. This means
            # that we can allow other courses to visit it later as we iterate through
            # each starting node.
            visited.remove(course)

            # Slight optimisation because we know that this course isn't a cycle therefore
            # we can reduce the time taken if we revisit the node.
            req_map[course] = []

        
            return True

        for course in range(numCourses):
            # If there is no valid course whereby there exists no cycles, then we return false
            # immediately as one instance of every node being a cycle means that you are unable
            # to complete them all.
            if not dfs(course):
                return False
        
        return True
        


print(Solution().canFinish(numCourses = 2, prerequisites = [[1,0]]))
            
        