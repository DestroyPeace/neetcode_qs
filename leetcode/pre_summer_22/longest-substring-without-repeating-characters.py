
"""def lengthOfLongestSubstring(s: str) -> int:
    s = list(s)
    longest_length = 0
    for index, value in enumerate(s):
        if s.count(value) != 1:
            s.remove(value)
            location = s.index(value) + 1
            s.insert(index, value)
            longest_length 

print(lengthOfLongestSubstring("pwwkew"))"""

def lengthOfLongestSubstring(s: str) -> int:
    character = {}
    left_pointer = {}
    result = 0 

    for r in range(len(s)):
        while s[r] in character:
            s.remove(s[left_pointer])
            left_pointer += 1
        character.add(s[r])
    
    result = max(result, r - left_pointer + 1 )

    return  result
