def main():
    from sys import stdin
    from itertools import islice
    tokens = map(int, stdin.read().split())
    N = next(tokens)
    boys = sorted(islice(tokens, N))
    M = next(tokens)
    girls = sorted(islice(tokens, M))

    if len(boys) < len(girls):
        smallest_array = boys
        biggest_array = girls
    else:
        smallest_array = girls
        biggest_array = boys

    ans = 0
    i = 0
    for x in smallest_array:
        while i < len(biggest_array) and biggest_array[i] <= x - 2:
            i += 1
        if i == len(biggest_array):
            break
        elif abs(biggest_array[i] - x) <= 1:
            ans += 1
            i += 1

    print(ans)

main()

"""
More elegant two-pointers solution:

http://codeforces.com/problemset/submission/489/38904003
R=lambda:sorted(map(int,raw_input().split()))
n,a,m,b=input(),R(),input(),R()
i=j=ans=0
while i<n and j<m:
	if abs(a[i]-b[j])<=1: ans+=1; i+=1; j+=1
	elif a[i]<b[j]: i+=1
	else: j+=1
print ans
"""