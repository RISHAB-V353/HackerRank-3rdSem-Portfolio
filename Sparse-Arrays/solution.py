# Problem 5: Sparse Arrays
# Time Complexity: O(N + Q) | Space Complexity: O(N)

from collections import Counter

def matchingStrings(stringList, queries):
    freq_map = Counter(stringList)
    return [freq_map[q] for q in queries]
