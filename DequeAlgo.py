from Basics import MyDeque

def palchecker(inputString):
    print inputString
    dq = MyDeque()
    dq.insertList(inputString)
    isPal = True
    print dq
    while (not dq.isEmpty() and dq.size()!=1):
        if dq.removeFront() != dq.removeRear():
            isPal = False
            break
    if(isPal==True):
        print "Yes Its A Palindrome!"
    else:
        print "Its Not A Palindrome!"
palchecker("lsdkjfskf")
palchecker("radar")