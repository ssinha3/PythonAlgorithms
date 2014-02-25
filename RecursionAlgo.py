#A recursive algorithm must have a base case.
#A recursive algorithm must change its state and move toward the base case.
#A recursive algorithm must call itself, recursively.
#Calculating the Sum of a List of Numbers
from Basics import MyStack
def listsum(lis):
    if(len(lis)==1):
        return lis[0]
    return lis[0] + listsum(lis[1:len(lis)])
print listsum([1,3,5,7,9])

#Converting an Integer to a String in Any Base
def convert(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return convert(n//base, base)+ convertString[n%base]

print(convert(1453,16))

#Iterative version with stack
rStack = MyStack()
def toStr(n,base):
    convertString = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            rStack.push(convertString[n])
        else:
            rStack.push(convertString[n % base])
        n = n // base
    res = ""
    while not rStack.isEmpty():
        res = res + str(rStack.pop())
    return res
print(toStr(1453,16))

#The tool we will use for our illustrations is Pythons turtle graphics module called turtle. The turtle module is standard with
# all versions of Python and is very easy to use. The metaphor is quite simple. You can create a turtle and the turtle can move
# forward, backward, turn left, turn right, etc. The turtle can have its tail up or down. When the turtles tail is down and the
# turtle moves it draws a line as it moves. To increase the artistic value of the turtle you can change the width of the tail as
# well as the color of the ink the tail is dipped in.
import turtle
myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)
#drawSpiral(myTurtle,200)
#myWin.exitonclick()

flag = True
def drawSnake(myTurtle, lineLen, flag=None):
    if lineLen > 0:
        if flag == True:
            myTurtle.forward(lineLen)
            myTurtle.right(90)
            drawSnake(myTurtle, lineLen-10, False)
        else:
            myTurtle.backward(lineLen)
            myTurtle.left(90)
            drawSnake(myTurtle, lineLen-10, True)

#drawSnake(myTurtle, 100, True)
#myWin.exitonclick()


def tree(branchLen,t):
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-15,t)
        t.left(40)
        tree(branchLen-15,t)
        t.right(20)
        t.backward(branchLen)

#t = turtle.Turtle()
#myWin = turtle.Screen()
#t.left(90)
#t.up()
#t.backward(100)
#t.down()
#t.color("green")
#tree(75,t)
#myWin.exitonclick()


def drawTriangle(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def getMid(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    drawTriangle(points,colormap[degree],myTurtle)
    if degree > 0:
        sierpinski([points[0],
                        getMid(points[0], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[1],
                        getMid(points[0], points[1]),
                        getMid(points[1], points[2])],
                   degree-1, myTurtle)
        sierpinski([points[2],
                        getMid(points[2], points[1]),
                        getMid(points[0], points[2])],
                   degree-1, myTurtle)

#myTurtle = turtle.Turtle()
#myWin = turtle.Screen()
#myPoints = [[-100,-50],[0,100],[100,-50]]
#sierpinski(myPoints,3,myTurtle)
#myWin.exitonclick()



#Tower of Hanoi
def moveDisk(fp,tp):
    print("moving disk from",fp,"to",tp)

def moveTower(height,fromPole, toPole, withPole):
    if height >= 1:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)
moveTower(3,"A","B","C")