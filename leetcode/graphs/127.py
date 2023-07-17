import collections 

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: str) -> int:
        if endWord not in wordList:
            return 0

        neighbours = collections.defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j + 1:]
                neighbours[pattern].append(word)

        visited = set([beginWord]) 
        q = collections.deque([beginWord])    

        # Init for default value (we start with one word)
        res = 1

        while q:
            for i in range(len(q)):
                word = q.popleft()

                if word == endWord:
                    return res 
                
                # Getting all of the neighbours.
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    
                    for nei in neighbours[pattern]:
                        if nei not in visited:
                            visited.append(nei)
                            q.append(nei)

            res += 1
        
        return 0
        

            

