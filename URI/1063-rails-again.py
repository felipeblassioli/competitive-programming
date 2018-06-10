def main():
    from collections import deque
    while True:
        N = int(input())
        if N == 0:
            break
        # rightmost element arrives first
        # leftmost element arrives last
        dir_a = deque(input().split(), N)
        dir_b = deque(input().split(), N)
        station = deque([], N)

        ans = ''
        while len(dir_b) > 0:
            # Target can be from dir_a or station
            # If it's neither we store in the station
            b = dir_b[0]
            if len(dir_a) > 0 and b == dir_a[0]:
                dir_a.popleft()
                dir_b.popleft()
                ans += 'IR'
            elif len(station) > 0 and b == station[-1]:
                station.pop()
                dir_b.popleft()
                ans += 'R'
            elif len(dir_a) > 0:
                ans += 'I'
                station.append(dir_a.popleft())
            else:
                break

        if len(dir_b) == 0:
            print(ans)
        else:
            print('%s Impossible' % ans)

main()