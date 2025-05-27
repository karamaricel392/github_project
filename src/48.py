import sys

def find_longest_substring(s):
    max_length = 0
    start = 0
    visited = set()

    for i in range(len(s)):
        if s[i] in visited:
            continue
        
        temp_start = i
        while s[temp_start] in visited:
            visited.add(s[temp_start])
            temp_start += 1

        max_length = max(max_length, i - start + 1)

        visited.clear()
        for j in range(start + 1, i + 1):
            if s[j] not in visited:
                visited.add(s[j])

    return max_length

s = input("Enter a string: ")
print(f"Length of the longest substring is {find_longest_substring(s)}")
