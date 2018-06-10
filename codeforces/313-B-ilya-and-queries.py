def main():
    from sys import stdin, stdout
    write = stdout.write

    tokens = iter(stdin.read().split())
    S = next(tokens)
    tokens = map(int, tokens)
    M = next(tokens)

    memo = [0] * len(S)
    for i in range(1, len(S)):
        if S[i] == S[i-1]:
            memo[i] = memo[i-1] + 1
        else:
            memo[i] = memo[i-1]

    ans = [ str(memo[r-1] - memo[l-1]) for l,r in zip(tokens, tokens) ]
    write('\n'.join(ans))

main()