def main():
    """
    Goal:
    The length of the maximum non-decreasing subsegment of sequence a.
    """
    from sys import stdin, stdout
    write = stdout.write
    tokens = map(int, stdin.read().split())
    N = next(tokens)
    A = list(tokens)

    dp = [0] * N
    dp[0] = 1
    ans = 1
    for i in range(1, N):
        if A[i-1] <= A[i]:
            dp[i] = dp[i-1] + 1
        else:
            dp[i] = 1
        ans = max(ans, dp[i])

    write(str(ans))

main()