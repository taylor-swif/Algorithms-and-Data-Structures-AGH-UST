"""Find the longest odd-length palindrome"""
def ceasar( s ):

    n = len(s)
    max_len = 1

    for i in range(1, n-1):
        
        j = 1
        curr_len = 1

        while i + j < n and i - j >= 0:

            if s[i-j] == s[i+j]:
                j += 1
                curr_len += 2
            else:
                break

        if curr_len > max_len:
            max_len = curr_len

    return max_len