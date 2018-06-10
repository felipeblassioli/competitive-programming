def main():
    """
    Let S := sum(A)
    A = Slice 1 + Slice 2 + Slice 3
    We want that each slice has a sum = S/3

    First we count how many times we can place i in such a way that slice 1 has sum = S/3
    For that we accumulate every element from A and keep note of every relevant sum.


    Now, if we are accumulating all elements, sometime we'll get the sum 2*S/3 (in this case slice 3 has sum S/3)
    This is equivalent to say that we found a j that gives a slice 3 of correct sum.
    In this case we need to update the answer:
    answer += (all positions that Slice 1 had the correct sum)

    Let count[i] := how many times Slice 1 has the sum S/3 until position i in the array
    """
    from sys import stdin
    from itertools import accumulate, tee, islice

    tokens = map(int, stdin.read().split())
    N = next(tokens)
    A, A2 = tee(tokens)
    S = sum(A2)

    if S % 3 != 0:
        print(0)
        return

    S1 = int(S/3)
    S2 = int(2*S/3)

    ans = count = 0
    
    # 2 <= i <= j <= N-1
    for s in islice(accumulate(A), N-1):
        if s == S2:
            ans += count
        if s == S1:
            count +=1

    print(ans)

main()