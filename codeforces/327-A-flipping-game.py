def main():
    """
    O(N) solution from the editorial: http://codeforces.com/blog/entry/8274

    Let S := number of ones in array A
    We want to maximize (S + number_of_ones_after_flip)
    S is constant, so we want to maximize number_of_ones_after_flip

    And number_of_ones_after_flip is the same as maximum contiguos array sum
    in the artificial array B[i] = +1 if A[i] == 0 and B[i] = -1 if A[i] == 1
    (everytime we flip a 1 we lose a unit in S)

    OBS: We need to make a flip (exactly one flip)
    For the input
    1 
    1
    The answer is 0
    """
    from sys import stdin, stdout
    write = stdout.write
    tokens = map(int, stdin.read().split())

    # 1 <= N <= 100
    N = next(tokens)
    A = list(tokens)

    S = sum(filter(lambda x: x == 1, A))
    B = [ -1 if x else 1 for x in A ]
    max_number_of_ones_after_flip = 0

    # Kadane Algorithm
    max_ending_in_i = max_number_of_ones_after_flip = B[0]
    for i in range(1, N):
        max_ending_in_i = max(B[i], max_ending_in_i + B[i])
        max_number_of_ones_after_flip = max(max_number_of_ones_after_flip, max_ending_in_i)
    
    write(str(S + max_number_of_ones_after_flip))

main()

"""
http://codeforces.com/problemset/submission/327/4019241
Equivalent kadane solution:
n = int(input())
a = list (map (int, input().split()))
one_count = 0
lcs,cur = 0,0
for i in a:
  if i == 1:
    one_count += 1
    cur = max (0, cur-1)
  else:
    cur += 1
    lcs = max (lcs, cur)
print ((one_count+lcs) if one_count != n else one_count-1)
"""


"""
Smaller solution:
http://codeforces.com/problemset/submission/327/4022236

n=input()
a=map(int,raw_input().split())
o=sum(a)
t=0
for i in range(n):
  for j in range(1,n-i+1):
    t=max(t,o+j-sum(a[i:i+j])*2)
print t

Similar to
http://codeforces.com/problemset/submission/327/10041065
n=input();
s=map(int,raw_input()[::2]);
print max(
    sum(s) # All original ones
    -2*sum(s[j:i]) # in the subsequence we flip we lose all ones there (times 2 because it was present in the original)
    +i -j # This is the count of zeros
    for i in range(n+1)for j in range(i))

1 0 0 1 0

2 - 1 1
i = 0 j = 2
0 1 1 1 0
"""
    
"""
http://codeforces.com/problemset/submission/327/14831950
DP solution?
n=int(input())
a=[int(i) for i in input().split()]
b=[[0 for i in range(100)]for j in range(100)]
#print(b)
if a[0]==1:
    b[0][0]=-1
else:
    b[0][0]=1
m=b[0][0]
for i in range(1,n):
    if a[i]==0:
        b[0][i]=b[0][i-1]+1
    else:
        b[0][i]=b[0][i-1]-1
    if b[0][i]>m:
        m=b[0][i]
for i in range(1,n):
    for j in range(i,n):
        if a[i-1]==1:
            b[i][j]=b[i-1][j]+1
        else:
            b[i][j]=b[i-1][j]-1
        if b[i][j]>m:
            m=b[i][j]
print(m+sum(a))
"""