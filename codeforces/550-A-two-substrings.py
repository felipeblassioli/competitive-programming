def main():
    """
    ABA and BAB can be either BA or AB we count them as mixed
    pure_AB is anything like AB?
    pure_BA is anything like BA?

    The way we count is:

    ABABAB = ABA BAB (mixed = 2)
    ABABXXXAB = ABA BXXX AB (mixed = 1, pure_AB = 1)
    """
    from sys import stdout
    s = input() + 'X'

    pure_AB = 0
    pure_BA = 0
    mixed = 0
    i = 0

    while i < len(s) - 1:
        substring = s[i-1] + s[i]
        if substring == 'AB':
            if s[i+1] == 'A':
                mixed += 1
                i += 3
            else:
                pure_AB += 1
                i += 2
        elif substring == 'BA':
            if s[i+1] == 'B':
                mixed += 1
                i += 3
            else:
                pure_BA += 1
                i += 2
        else:
            i += 1

    if pure_AB > 0 and pure_BA > 0:
        stdout.write('YES')
    elif mixed > 0 and (pure_AB > 0 or pure_BA > 0):
        stdout.write('YES')
    elif mixed >= 2:
        stdout.write('YES')
    else:
        stdout.write('NO')

main()