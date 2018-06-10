def main():
    """
    Problem constraints
    1 <= N,A,B,C <= 4000

    DP solution
    Let 
    dp[i] := maximum number of pieces for a ribbon of length i
    # Given a riboon with length i, we choose the best of 3 options:
    # Cutting a piece of lenght A or B or C
    # If I cut a piece of length A, the best I can do is best[i - A] pieces + 1 piece
    dp[i] := 1 + max(dp[i-A], dp[i-B], dp[i-C])
    dp[0] := 0
    dp[i < 0] := -Infinity
    """
    N, A, B, C = map(int, input().split())

    dp = [-9999] * 4001
    dp[0] = 0
    for i in range(1, N+1):
        dp[i] = 1 + max(dp[i-A], dp[i-B], dp[i-C])

    print(dp[N])
    
main()