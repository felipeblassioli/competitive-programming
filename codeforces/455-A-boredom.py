def main():
    #
    # Important observations:
    #   1) If we choose a number X, then we score X * frequency_that_X_appears in the input array
    #   2) 1 <= N <= 10**5 so we need to construct a single dimensional dp
    #   3) Each element 1<= A[k] <= 10 ** 5 (same as N)
    #   4) For all distinct numbers in the input, We can either: 
    #      a) choose/delete a number (in this case we score something)
    #      b) ignore it (in this case we do not gain points)
    #
    # Let dp[i] := maximum points for a sequence with elements <= i
    # The state i domain is related to A[k] (not the number of elements in the array!)
    # dp[0] = 0 , because by problem definition there's no 0 in the input
    # dp[1] = 1 * frequency_of_1_in_the_input_array
    # dp[i] = ?
    # For a given number i, if we choose it we can get at best:
    # Case 1:
    #   (i * frequency_i_in_input + maximum points for a sequence with elements <= i-2) points, because
    #   we had to delete all i-1 points.
    # Case 2:
    #   We ignore number i (so we do not need to delete i-1), in this case our max points is:
    #   dp[i-1] = maximum points for a sequence with element <= i-1
    #
    # Solution is O(N) because of observation (3)
    from sys import stdin
    from collections import Counter

    tokens = map(int, stdin.read().split())
    N = next(tokens) 
    counter = Counter(tokens)
    biggest_element = max(counter.keys()) + 1

    dp = [0] * biggest_element
    # dp[0] = 0
    dp[1] = counter[1]
    for i in range(2, biggest_element):
        dp[i] = max(dp[i-1], i * counter[i] + dp[i-2])

    print(dp[biggest_element - 1])

main()

"""
http://codeforces.com/problemset/status/455/problem/A
Using less memory:
n=int(input())
s=[0]*1000001
for i in map(int,input().split()):
	s[i]+=i
a=b=0
for d in s:
	a,b=max(a,b+d),a
print(a)
"""