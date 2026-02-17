#Smart Calculator
def calculate(expression: str)-> float:
    expression = expression.replace(" ","")
    stack = []
    num = 0
    sign = '+'
    i=0
    while i<len(expression):
        ch=expression[i]
        if ch.isdigit():
            num=num*10+int(ch)
        if(not ch.isdigit()) or i==len(expression)-1:
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop()*num)
            elif sign == '/':
                stack.append(stack.pop()/num)
            sign = ch
            num = 0
        i+=1
    result = float(sum(stack))
    return round(result,2)
print(calculate("2 + 3"))
print(calculate("10 - 5 * 2"))
print(calculate("20 / 4 + 3 * 2"))
print(calculate("100 / 3"))
print(calculate("5"))
