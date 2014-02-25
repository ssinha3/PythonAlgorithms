from Basics import MyStack
import time

def parChecker(inputString):
    st = MyStack()
    for element in inputString:
        if(element == '('): #if a left bracket
            st.push(element)
        else:#its a right bracket
            st.pop()
    if(st.isEmpty()):
        print("Expression is Valid")
    else:
        print("Expression is Invalid")

def sumN(n):
    start = time.time()
    theSum=0
    for x in range(n+1):
        theSum = theSum + x
    print theSum
    end = time.time()
    print "Execution Time, ", end-start

parChecker('((()))')
parChecker('(()')
sumN(5000)

#Check for Anagrams O(1)
def anagramSolution(firstString, secondString):
    firstDict = dict()
    if(len(firstString)!=len(secondString)):
        return False
    for element in firstString:
        if(firstDict.has_key(element)):
            firstDict[element] = firstDict.get(element) + 1
        else:
            firstDict[element] = 1
    for element in secondString:
        if(firstDict.has_key(element)):
            firstDict[element] = firstDict[element] - 1
    for x in firstDict.values():
       if(x != 0):
           return False

    return True


print(anagramSolution('apple','pleap'))

# Note: Recursion internally uses stack!
def decimalToBinary(num):
    if(num==0 or num==1):
        return str(num)
    remainder = num % 2
    return decimalToBinary(num/2) + str(remainder)

print(decimalToBinary(42))

#Infix-to-Postfix Conversion
def infixToPostFix(infixString):
    stOperator = MyStack()
    stOperand = MyStack()
    precedence = dict()
    precedence['/'] = 3
    precedence['*'] = 3
    precedence['+'] = 2
    precedence['-'] = 2
    precedence['('] = 1
    for element in infixString:
        if(element in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' or element in '1234567890'):
            stOperand.push(element)
        elif(element in '('):
            stOperator.push(element)
        elif(element in ')'):
            while(stOperator.peek()!='('):
                sec = stOperand.pop()
                fir = stOperand.pop()
                opr = stOperator.pop()
                stOperand.push(fir+sec+opr)
            stOperator.pop()
        else:# its an operator
            if(stOperator.isEmpty()):
                stOperator.push(element)
            else:
                if(precedence[element] >= precedence[stOperator.peek()]):
                    stOperator.push(element)
                else:
                    sec = stOperand.pop()
                    fir = stOperand.pop()
                    opr = stOperator.pop()
                    stOperator.push(element)
                    stOperand.push(fir+sec+opr)
    if(stOperator.isEmpty() and not stOperand.isEmpty()):
        print 'error'
    else:
        while(not stOperator.isEmpty()):
            if(not stOperand.isEmpty()):
                sec = stOperand.pop()
                fir = stOperand.pop()
            opr = stOperator.pop()
            stOperand.push(fir+sec+opr)
    print stOperand.peek()

infixToPostFix("A*B+C*D")
infixToPostFix("(A+B)*C-(D-E)*(F+G)")

def postfixEval(postfixExpr):
    operandStack = MyStack()
    tokenList = postfixExpr.split()
    for token in tokenList:
        if token in "0123456789":
            operandStack.push(int(token))
        else:
            operand2 = operandStack.pop()
            operand1 = operandStack.pop()
            result = doMath(token,operand1,operand2)
            operandStack.push(result)
    return operandStack.pop()

def doMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval('7 8 + 3 2 + /'))
