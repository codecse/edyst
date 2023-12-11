def climbing_leaderboard(scores, chacha_scores):
    unique_scores = sorted(set(scores), reverse=True)
    rankings = []

    i = len(unique_scores) - 1  # Start from the last position of the leaderboard

    for chacha_score in chacha_scores:
        while i >= 0 and chacha_score >= unique_scores[i]:
            i -= 1  # Move down the leaderboard until finding the correct rank

        rankings.append(i + 2)  # Chacha's rank is one more than the index (0-based) where her score should be inserted

    return rankings

# Example usage:
n = int(input())
leaderboard_scores = list(map(int, input().split()))
m = int(input())
chacha_scores = list(map(int, input().split()))

result = climbing_leaderboard(leaderboard_scores, chacha_scores)
for rank in result:
    print(rank)
