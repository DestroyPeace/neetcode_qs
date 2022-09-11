def consecutive_ones(number):
    start = 0
    longest = 0

    for end in range(len(number)):
        while number[start : end + 1].count(0) > 0:
            start += 1
        
        if len(number[start : end + 1]) > longest:
            longest = len(number[start : end + 1]) 
        
    return max(longest, end - start + 1)

print(consecutive_ones([1,1,0,1,1,1]))