def main():
    from sys import stdin, stdout
    from itertools import islice

    tokens = map(int, stdin.read().split())
    N = next(tokens)
    K = next(tokens)
    Hs = list(tokens)

    ans = 0
    minimum_sum = current_sequence_sum = sum(islice(Hs, K))
    for i in range(1, N-K+1):
        current_sequence_sum += (Hs[i+K-1] - Hs[i-1])
        minimum_sum = min(current_sequence_sum, minimum_sum)

        if current_sequence_sum <= minimum_sum:
            ans = i

    print(ans+1)

main()