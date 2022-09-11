def longestPalindrome(s):
    palindromes = []
    for start in range(len(s) + 1):
        for end in range(len(s) + 1):
            if s[start:end] == "".join(list(reversed(s[start:end]))) and s[start:end] != "":
                print(f"{s[start:end]} is a palindrome")
                palindromes.append(s[start:end])
    
    print(sorted(palindromes, key = lambda x: len(str(x)), reverse = True))
    return sorted(palindromes, key = lambda x: len(str(x)), reverse = True)[0]

print(longestPalindrome(input()))