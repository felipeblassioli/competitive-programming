def main():
    from collections import deque
    from sys import stdin
    for line in stdin:
        parentheses = filter(lambda c: c == '(' or c == ')', line)
        stk = deque([], len(line)-1)
        left_parentheses_count = 0
        right_parentheses_count = 0

        c = next(parentheses, None)
        if c == ')':
            # unmatched first parentheses
            print('incorrect')
            continue
        elif c == '(':
            left_parentheses_count += 1
            stk.append(c)
        
        c = next(parentheses, None)
        while c is not None:
            if c == '(':
                left_parentheses_count += 1
                stk.append(c)
            elif len(stk) > 0:
                right_parentheses_count += 1
                stk.pop()
            else:
                right_parentheses_count += 1
                break
            c = next(parentheses, None)

        if left_parentheses_count == right_parentheses_count: 
            print('correct')
        else:
            print('incorrect')

main()

