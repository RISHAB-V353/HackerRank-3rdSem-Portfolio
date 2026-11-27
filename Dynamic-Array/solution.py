# Problem 2: Dynamic Array
# Time Complexity: O(N + Q) | Space Complexity: O(N)

def dynamicArray(n, queries):
    seq_list = [[] for _ in range(n)]
    last_answer = 0
    results = []

    for q_type, x, y in queries:
        idx = (x ^ last_answer) % n
        if q_type == 1:
            seq_list[idx].append(y)
        elif q_type == 2:
            last_answer = seq_list[idx][y % len(seq_list[idx])]
            results.append(last_answer)

    return results
