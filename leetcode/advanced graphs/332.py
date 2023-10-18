List = list 

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {src : [] for src, _ in tickets}

        tickets.sort()
        for src, dst in tickets:
            adj[src].append(dst)

        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True 
            if src not in adj:
                return False 
            
            # Using a temporary list as this ensures that we can work off this list as we mutate the other 
            # proper adjacency list, essentially a deep copy of the list.
            temp = list(adj[src])

            # Finding each possible path that is possible from the current temp (list of possible ticket destinations)
            # by calculating the DFS path for the values
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)

                # If a possible completed path occurs, use that path and essentially use greedy knowing
                # that you have constrained the paths to be the most lexical path already.
                if dfs(v):
                    return True 
                
                # This allows for another combination of tickets to be tested.
                adj[src].insert(i, v)

                # Removing the ticket combination from the results. by removing the res.
                res.pop()
            
            return False

        # Knowing that we always start at JFK.
        dfs("JFK")

        return res

    

test = Solution()
test.findItinerary(tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]])