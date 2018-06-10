def main():
    """
    We want the largest odd number, so we sum everything
    and if the sum is even, we subtract the minium odd number.
    
    OBS:
      - I was afraid to use print() because statement said print a single number (no newline)
    """
    from sys import stdin, stdout
    from itertools import islice

    write = stdout.write
    tokens = map(int, stdin.read().split())
    N = next(tokens)
    numbers = sorted(islice(tokens, N))

    total = sum(numbers)
    if total % 2 == 0:
        m = min(filter(lambda x: x % 2 == 1, numbers), default=total)
        write(str(total - m))
    else:
        write(str(total))

main()