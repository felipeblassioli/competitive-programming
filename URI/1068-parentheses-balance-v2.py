def main():
    from sys import stdin
    for line in stdin:
        parentheses = filter(lambda c: c == '(' or c == ')', line)
        left_parentheses_count = 0

        c = next(parentheses, None)
        if c == ')':
            # unmatched first parentheses
            print('incorrect')
            continue
        elif c == '(':
            left_parentheses_count += 1
        
        c = next(parentheses, None)
        while c is not None:
            if c == '(':
                left_parentheses_count += 1
            elif left_parentheses_count > 0: 
                left_parentheses_count -= 1
            else:
                left_parentheses_count -= 1
                break
            c = next(parentheses, None)

        if left_parentheses_count == 0: 
            print('correct')
        else:
            print('incorrect')

main()

