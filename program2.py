def decode_message(message, pattern):
    # Memoization dictionary to avoid recalculating
    memo = {}
    
    # Recursive function to check match
    def is_match(i, j):
        # If we have checked this state before, return its result
        if (i, j) in memo:
            return memo[(i, j)]
        
        # If we've reached the end of both message and pattern, it's a match
        if j == len(pattern):
            return i == len(message)

        if pattern[j] == '*':

            match = (is_match(i, j + 1) or (i < len(message) and is_match(i + 1, j)))
            memo[(i, j)] = match
            return match
        
        if i < len(message) and (pattern[j] == '?' or pattern[j] == message[i]):
            memo[(i, j)] = is_match(i + 1, j + 1)
            return memo[(i, j)]
        

        memo[(i, j)] = False
        return False
    
    return is_match(0, 0)
