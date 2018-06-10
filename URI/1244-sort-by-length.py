def main():
    N = int(input())
    for _ in range(N):
        print(' '.join(sorted(input().split(), key = lambda w: len(w), reverse=True)))

main()