# Problem 1: Diagonal Difference
# Time Complexity: O(N) | Space Complexity: O(1)

def diagonalDifference(arr):
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0

    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n - 1 - i]

    return abs(primary_sum - secondary_sum)
