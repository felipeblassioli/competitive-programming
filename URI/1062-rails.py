def main():
    from collections import deque
    while True:
        N = int(input())
        if N == 0:
            break
        while True:
            # 1 arrives first N arrives last
            dir_a = deque(map(str, range(N,0,-1)), N)
            dir_b = deque(input().split(), N)
            station = deque([], N)
            if len(dir_b) == 1:
                print('')
                break

            while len(dir_b) > 0:
                # Target can be from dir_a or station
                # If it's neither we store in the station
                b = dir_b[0]
                if len(dir_a) > 0 and b == dir_a[-1]:
                    dir_a.pop()
                    dir_b.popleft()
                elif len(station) > 0 and b == station[-1]:
                    station.pop()
                    dir_b.popleft()
                elif len(dir_a) > 0:
                    station.append(dir_a.pop())
                else:
                    break

            if len(dir_b) == 0:
                print('Yes')
            else:
                print('No')

main()