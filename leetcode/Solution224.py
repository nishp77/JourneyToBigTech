
result = []
test = "((3/2)-(2+3))"
for c in test:
        if c == ')':
            total = 0
            while result[-1] != '(':
                a = int(result.pop())
                operand = result.pop()
                b = int(result.pop())

                if operand == '+':
                    total = b+a
                elif operand == '-':
                    total = b-a
                elif operand == '*':
                    total = a*b
                elif operand == '/':
                    total = b/a
            
            result.pop()
            result.append(total)

        else:
            result.append(c)

print(result)
