# Problem 4: Compare the Triplets
# Time Complexity: O(1) | Space Complexity: O(1)

def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0

    for alice_val, bob_val in zip(a, b):
        if alice_val > bob_val:
            alice_score += 1
        elif alice_val < bob_val:
            bob_score += 1

    return [alice_score, bob_score]
