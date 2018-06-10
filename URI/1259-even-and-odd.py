def main():
    from sys import stdin, stdout
    from itertools import tee

    tokens = map(int, stdin.read().split())
    _ = next(tokens)

    evens, odds = tee(tokens)
    evens = filter(lambda n: n % 2 == 0, evens) 
    odds = filter(lambda n: n % 2 == 1, odds)

    ans = map(str, sorted(evens))
    stdout.write('\n'.join(ans))
    stdout.write('\n')
    ans = map(str, sorted(odds, reverse=True))
    stdout.write('\n'.join(ans))
    stdout.write('\n')


main()