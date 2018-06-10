# https://csacademy.com/contest/archive/task/max-even-subarray/ - Date: 2018-06-08
# You are given an array of NN elements. Find the subarray of maximum sum having even length.
def main():
    # Take as input:
    # 1 -2 3 -4 5 -6
    # Since we need a subarray of even length, our current pair (i-1, i)
    # dp[0] = 0
    # dp[1] = A[0] + A[1] (The first pair)
    # dp[i] = max(A[i-1] + A[i], A[i-1] + A[i] + dp[i-2])
    #
    # We define dp[i] as the maximum sum of all even length subarrays ending at A[i]
    # Solution using DP is O(N)
    from sys import stdin, stdout
    tokens = map(int, stdin.read().strip().split())
    N = next(tokens)
    tokens = list(tokens)

    dp = [0] * N
    dp[1] = tokens[0] + tokens[1]
    ans = dp[1]
    for i in range(2, len(tokens)):
        acc = tokens[i-1] + tokens[i] + dp[i-2]
        dp[i] = max(acc, tokens[i-1] + tokens[i])
        ans = max(dp[i], ans)

    print(ans)

main()

"""
def main():
    # Naive O(N^2) solution recalculates all even lengths subarrays for each element
    from sys import stdin, stdout
    tokens = map(int, stdin.read().strip().split())
    N = next(tokens)

    tokens = list(tokens)

    #Naive solution is O(N^2) and TLE for N=10000

    ans = -10**9 - 1

    for i in range(1, len(tokens)):
        acc = tokens[i] + tokens[i-1]
        ans = max(ans, acc)
        for j in range(i-3, -1, -2):
            acc += tokens[j] + tokens[j+1]
            ans = max(ans, acc)
            
    print(ans)
"""
