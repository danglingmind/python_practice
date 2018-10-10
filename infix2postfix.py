import stack as st
# postfix conversion
def postfixConv(inStr):
    opStack = st.stack()
    postFixStr = []
    # precedence of every operator
    prc = {"*":3,
           "/":3,
           "+":2,
           "-":2,
           "(":1}

    # start iterating over the string
    for token in inStr:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            # push it into the output string
            postFixStr.append(token)
        elif token == '(':
            # push into opStack
            opStack.push(token)
        elif token == ')':
            # pop until (
            topItem = opStack.pop()
            while topItem != '(':
                postFixStr.append(topItem)
                topItem = opStack.pop()
        else:
            # pop the items according to the precedence of the comming operators
            while not opStack.isEmpty() and (prc[token] < prc[opStack.top()]):
                postFixStr.append(opStack.pop())
            # push the current token into the opStack 
            opStack.push(token)

    # append all the remaining items to output string
    while not opStack.isEmpty():
        postFixStr.append(opStack.pop())

    return " ".join(postFixStr)


print(postfixConv("(A+B)*C-(D-E)*(F+G)"))

