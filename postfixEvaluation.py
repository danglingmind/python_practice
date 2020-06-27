import stackImpl as st 

def doMath(op1, op2, operand):
    if operand == "+":
        return op1 + op2
    elif operand == "-":
        return op1-op2
    elif operand == "*":
        return op1*op2
    else :
        return op1/op2

def evalPostFixExp(postFixExp):
    evalStack = st.stack()
    for token in postFixExp:
        if token in "0123456789":
            evalStack.push(int(token))
        else :
            op1 = evalStack.pop()
            op2 = evalStack.pop()
            res = doMath(op1, op2, token)
            evalStack.push(res)

    return evalStack.pop()

# drive 
print(evalPostFixExp("456*+"))

