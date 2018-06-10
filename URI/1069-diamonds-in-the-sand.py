def main():
    from collections import deque

    N = int(input())
    for _ in range(N):
        line = input()

        stk = deque([], len(line))
        ans = 0
        for c in line:
            if c == '<':
                stk.append(c)
            elif c == '>' and len(stk) > 0:
                stk.pop()
                ans += 1
        print(ans)

main()

