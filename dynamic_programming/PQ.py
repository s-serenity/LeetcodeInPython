# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(P, Q):
    # Implement your solution here
    n = len(P)
    dp = [1] * n
    distinct_letters = set()
    distinct_letters.add(P[0])
    distinct_letters.add(Q[0])
    for i in range(1, n):
        if P[i] not in distinct_letters and Q[i] not in distinct_letters:
            dp[i] = dp[i - 1] + 1
            distinct_letters.add(P[i])
            distinct_letters.add(Q[i])
        else:
            if P[i] in distinct_letters or Q[i] in distinct_letters:
                dp[i] = dp[i - 1]

    return dp[n - 1]

P = 'abc'
Q = 'bcd'
solution(P,Q)