def main():
    """
    We try all slices of size N to find the best one.
    Example:

    N=4 M=10
    a = [1 2 3 4 5 8 8 8 8 10]

    We start with a[4-1] - a[3 - 4 + 1] = 4 - 1 = 3
    Further we find the slice [8,8,8,8] with the diff = 0
    """
    from sys import stdout
    N, M = map(int, input().split())
    pieces = sorted(map(int, input().split()))

    ans = min(pieces[i] - pieces[i - N + 1] for i in range(N-1, M))
    stdout.write(str(ans))

main()