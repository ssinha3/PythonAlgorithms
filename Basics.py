#Tutorial From http://interactivepython.org/courselib/static/pythonds/index.html
# Material Reference: http://interactivepython.org/courselib/static/pythonds/index.html and is authority of the author only.
# My aim is to learn python data structures
import math

print('This is a sample print')
print 'This is another sample print'
print 2 * 5
print 2 ** 4
print 7 % 3
print 7 / 3 + 7 % 3
#Python has two main built-in numeric classes that implement the integer and floating point data types.
# These Python classes are called int and float. The standard arithmetic operations, +, -, *, /, and **
# (exponentiation), can be used with parentheses forcing the order of operations away from normal operator precedence.
# Other very useful operations are the remainder (modulo) operator, %, and integer division, //.
# Note that when two integers are divided, the result is a floating point. The integer division operator returns the
# integer portion of the quotient by truncating any fractional part.

print True
print not True
print not (True or False)
print not (True and False)
print 5 == 10
print 5 == 10 or 5 < 10
print 5 <= 10 and 10 >= 5

#Identifiers are used in programming languages as names. In Python,
# identifiers start with a letter or an underscore (_), are case sensitive, and can be of any length.
sum = 0
sum = sum + 1
print sum

#A list is an ordered collection of zero or more references to Python data objects.
# Lists are written as comma-delimited values enclosed in square brackets. The empty list is simply
# [ ]. Lists are heterogeneous, meaning that the data objects need not all be from the same class and the
# collection can be assigned to a variable as below
list = [True, 1, 'echo', 6.7]
print list
print 'List value at index i', list[0] #accessing a list
list2 = [True, 2, 'echo2', 6.5]
print list2
print list + list2 # concat lists
print list*2
print 'If true exists in list,', True in list
print 'Length Of List, ', len(list) #length of a list
listEcho = ['echo 0', 'echo 1', 'echo 2', 'echo 3']
#Note that the indices for lists (sequences) start counting with 0. The slice operation, myList[1:3],
# returns a list of items starting with the item indexed by 1 up to but not including the item indexed by 3.
print listEcho[0:3] #slicing a list
#append	alist.append(item)	Adds a new item to the end of a list
#insert	alist.insert(i,item)	Inserts an item at the ith position in a list
#pop	alist.pop()	Removes and returns the last item in a list
#pop	alist.pop(i)	Removes and returns the ith item in a list
#sort	alist.sort()	Modifies a list to be sorted
#reverse	alist.reverse()	Modifies a list to be in reverse order
#del	del alist[i]	Deletes the item in the ith position
#index	alist.index(item)	Returns the index of the first occurrence of item
#count	alist.count(item)	Returns the number of occurrences of item
#remove	alist.remove(item)	Removes the first occurrence of item
itemList = ['item 0', 'item 1', 'item 2', 'item 3']
print itemList
itemList.append('item 4')
print itemList
itemList.insert(1, 'item 11')
print itemList
itemList.pop()
print itemList
itemList.pop(0)
print itemList
itemList.sort()
print itemList
itemList.reverse()
print itemList
del itemList[2]
print itemList
print itemList.index('item 2')
itemList.append('item 2')
print itemList
print itemList.count('item 2')
itemList.remove('item 2')
print itemList

print (55).__add__(22)

# range function. range produces a range object that represents a sequence of values. By using the list function,
# it is possible to see the value of the range object as a list.
# note it doesn't print till 10!!the sequence starts with 0 and goes up to but does not include 10
print range(0,10)
print range(0,10,2)
print range(-1,10,2)

name = "shayan"
print name
print name[0]
print name*2
print name.upper()
print name.find('h')
#If no division is specified, the split method looks for whitespace characters such as tab, newline and space.
print name.split('y')
print name.count('a')
print name.center(10)
print name.ljust(10)
print name.rjust(10)
print name.find('a') #returns index of first occurence
print name.lower()

#A major difference between lists and strings is that lists can be modified while strings cannot.
# This is referred to as mutability. Lists are mutable; strings are immutable.
# name[0] = 'D' Invalid and will throw and error
print name

#Tuples are very similar to lists in that they are heterogeneous sequences of data. The difference is that a tuple is
# immutable, like a string. A tuple cannot be changed. Tuples are written as comma-delimited values enclosed in parentheses.
# methods match that of lists
myTuple = (1, 1.5, True, 'Jacob')
print myTuple
print len(myTuple)
print myTuple[3]
print myTuple*3
print myTuple
print myTuple[0:2]
#myTuple[0] = 2 Immutable, will throw an error
#print myTuple

#A set is an unordered collection of zero or more immutable Python data objects. Sets do not allow duplicates and
# are written as comma-delimited values enclosed in curly braces. The empty set is represented by set().
# Sets are heterogeneous, and the collection can be assigned to a variable as below.
#Even though sets are not considered to be sequential, they do support a few of the familiar operations presented earlier.
mySet = {3, 6, "cat", 5.5, False}
print mySet
print len(mySet)
print 3 in mySet
mySet2 = {4, 7, "dog", 5.5, True}
print mySet | mySet2
print mySet2 & mySet
print mySet - mySet2
# <= Asks whether all elements of the first set are in the second, i.e. s1 <= s2 means is s1 a subset of s2
print mySet <= mySet2
print mySet <= mySet
print mySet.union(mySet2)
print mySet.intersection(mySet2)
print mySet.difference(mySet2)
mySet.add('Test')
print mySet
mySet.remove('Test')
print mySet
print mySet.pop()
mySet.clear()
print mySet

# Dictionaries are collections of associated pairs of items where each pair consists of a key and a value.
# This key-value pair is typically written as key:value. Dictionaries are written as comma-delimited key:value
# pairs enclosed in curly braces.
# We can manipulate a dictionary by accessing a value via its key or by adding another key-value pair.
# The syntax for access looks much like a sequence access except that instead of using the index of the item we use the key value.
# dictionary is maintained in no particular order with respect to the keys.
dic = {'key 1':'value 1', 'key 2':'value 2', 'key 3':'value 3', 'key 4':'value 4'}
print dic
print dic['key 2']
dic['key 2'] = 'modified value 2'
print dic

# use the list function to convert them to lists
print dic['key 1']
print 'key 2' in dic
del dic['key 1']
print dic
print dic.keys()
print dic.values()
print dic.items()
print dic.get('key 2')
#adict.get(k,alt)	Returns the value associated with k, alt otherwise
print dic.get('key 0', 'Not Found')

#sradius = input("Please enter the radius of the circle ")
#radius = float(sradius)
#print 22/7 * radius * radius

# String formatting  The % operator is a string operator called the format operator. The left side of the expression holds the
# template or format string, and the right side holds a collection of values that will be substituted into the format string.
# Note that the number of values in the collection on the right side corresponds with the number of % characters in the format string.

print("Hello")
print("Hello","World")
#print("Hello","World", sep="---")
aName = 'Shayan'
age = 10
print("%s" % aName)
print("%s brain is %d years old." % (aName, age))

#A conversion character tells the format operator what type of value is going to be inserted into that position in the string.
# In the example above, the %s specifies a string, while the %d specifies an integer. Other possible type specifications include
# i, u, f, e, g, c, or %.
#number	%20d	Put the value in a field width of 20
#-	%-20d	Put the value in a field 20 characters wide, left-justified
#+	%+20d	Put the value in a field 20 characters wide, right-justified
#0	%020d	Put the value in a field 20 characters wide, fill in with leading zeros.
#.	%20.2f	Put the value in a field 20 characters wide with 2 characters to the right of the decimal point.
#(name)	%(name)d	Get the value from the supplied dictionary using name as the key.
#d, i	Integer
#u	Unsigned integer
#f	Floating point as m.ddddd
#e	Floating point as m.ddddde+/-xx
#E	Floating point as m.dddddE+/-xx
#c	Single character
#s	String, or any Python data object that can be converted to a string by using the str function.
#%	Insert a literal % character
price = 24
item = "banana"
print("The %s costs %d cents" % (item,price))
print("The %+10s costs %5.2f cents" % (item,price))
print("The %+10s costs %10.2f cents" % (item,price))
itemdict = {"item":"banana", "cost":24}
print("The %(item)s costs %(cost)7.1f cents"%itemdict)

# while loop
i = 0
while (i < 10):
    print "hello, ",i
    i = i + 1

for i in range(0,10):
    print "hello, ",i

listWords = ["cat", "dog", "bat"]
letterlist = [ ]
for word in listWords:
    for l in word:
        letterlist.append(l)

print letterlist

n=64
if(n<65):
    print(math.sqrt(n))
else:
    print 'Reduce the number!'

# using elif

a=20
b=10
if(a==b):
    print 'Equal'
elif(a>b):
    print 'a>b'
else:
    print 'a<b'

#Note: we can or cannot have brackets!
#Returning to lists, there is an alternative method for creating a list that uses iteration and selection constructs.
# The is known as a list comprehension. A list comprehension allows you to easily create a list based on some processing
# or selection criteria.
#The variable x takes on the values 1 through 10 as specified by the for construct. The value of x*x is then computed
# and added to the list that is being constructed. The general syntax for a list comprehension also allows a selection
# criteria to be added so that only certain items get added

sampleList = [1, 2, 3, 4, 5]
print [x*x for x in sampleList if(x*x>10)]
# Any sequence that supports iteration can be used within a list comprehension to construct a new list.
batList = ['bat', 'cat', 'mat', 'dog']
updatedbatList = []
vowels = ['a', 'e', 'i', 'o', 'u']
print [letter.upper() for word in batList for letter in word if(letter not in vowels)]

#n this case, the Python interpreter has found that it cannot complete the processing of this instruction since it does
# not conform to the rules of the language. Syntax errors are usually more frequent when you are first learning a language.
#The other type of error, known as a logic error, denotes a situation where the program executes but gives the wrong result.
# This can be due to an error in the underlying algorithm or an error in your translation of that algorithm. In some cases,
# logic errors lead to very bad situations such as trying to divide by zero or trying to access an item in a list where the
# index of the item is outside the bounds of the list. In this case, the logic error leads to a runtime error that causes
# the program to terminate. These types of runtime errors are typically called exceptions.
#Most of the time, beginning programmers simply think of exceptions as fatal runtime errors that cause the end of execution.
# However, most programming languages provide a way to deal with these errors that will allow the programmer to have some type
# of intervention if they so choose. In addition, programmers can create their own exceptions if they detect a situation in the
# program execution that warrants it.
#When an exception occurs, we say that it has been raised.You can handle the exception that has been raised by using a try statement.
# For example, consider the following session that asks the user for an integer and then calls the square root function from the math library.
# If the user enters a value that is greater than or equal to 0, the print will show the square root. However, if the user enters a negative
# value, the square root function will report a ValueError exception.

# uncomment o run!
#num = int(input("Please Enter A Number of Which You Want To Find The Square Root Of: "))
#try:
#    print math.sqrt(num)
#except:
#    print "You Have Given A Bad Value"

#It is also possible for a programmer to cause a runtime exception by using the raise statement. For example,
# instead of calling the square root function with a negative number, we could have checked the value first and
# then raised our own exception. The code fragment below shows the result of creating a new RuntimeError exception.

# uncomment o run!
#num1 = float(input("Please enter a float number"))
#if(num1<0):
#    try:
#        raise RuntimeError("Give a valid number!")
#    except:
#        print ("Who Dat!")


# Defining functions

def getSquareRoot(n):
    return math.sqrt(n)

print getSquareRoot(16)


#def squareroot(n): Gives error need to check more
#    root = n/2    #initial guess will be 1/2 of n
#    for k in range(20):
#        root = (1/2)*(root + (n / root))
#    return root
#
#print squareroot(9)

#In Python, we define a new class by providing a name and a set of method definitions that are syntactically similar to function definitions.
#provides the framework for us to define the methods. The first method that all classes should provide is the constructor. The constructor
# defines the way in which data objects are created. To create a Fraction object, we will need to provide two pieces of data, the numerator
# and the denominator. In Python, the constructor method is always called __init__ (two underscores before and after init)
#Notice that the formal parameter list contains three items (self, top, bottom). self is a special parameter that will always be used as a
# reference back to the object itself. It must always be the first formal parameter; however, it will never be given an actual parameter
# value upon invocation. As described earlier, fractions require two pieces of state data, the numerator and the denominator. The notation
# self.num in the constructor defines the fraction object to have an internal data object called num as part of its state. Likewise, self.den
# creates the denominator. The values of the two formal parameters are initially assigned to the state, allowing the new fraction object to
# know its starting value.To create an instance of the Fraction class, we must invoke the constructor. This happens by using the name of
# the class and passing actual values for the necessary state (note that we never directly invoke __init__).
class Fraction:

    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def show(self):
        print self.num,"/",self.den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)

    def gcd(self, m, n):
        while m%n != 0:
            oldm = m
            oldn = n

            m = oldn
            n = oldm%oldn
        return n

    def __add__(self, otherfraction):
        newNum = self.num * otherfraction.den + self.den * otherfraction.num
        newDen = self.den * otherfraction.den
        common = self.gcd(newNum,newDen)
        return Fraction(newNum//common, newDen//common)

    def __eq__(self, other):
        return (self.num * other.den == self.den * other.num)

myfraction = Fraction(3,5)
print myfraction
f1 = Fraction(1,2)
f2 = Fraction(2,4)
print f1+f2
print(f1 == f2)

#Inheritance And Oops!
# All logic gates will have some name(label) and one output line
class LogicGate:

    def __init__(self,n):
        self.name = n
        self.output = None

    def getName(self):
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getName()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getName()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0

class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getName()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

#
#def main():
#   g1 = AndGate("G1")
#   g2 = AndGate("G2")
#   g3 = OrGate("G3")
#   g4 = NotGate("G4")
#   c1 = Connector(g1,g3)
#   c2 = Connector(g2,g3)
#   c3 = Connector(g3,g4)
#   print(g4.getOutput())
#
#main()

class MyStack:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) -1]

    def size(self):
        return len(self.items)

s = MyStack()
print(s.isEmpty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())




class MyQueue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[0]

    def isEmpty(self):
        return len(self.items)==0


print "Check Queue!"
q=MyQueue()
print q.isEmpty()
q.enqueue('dog')
q.enqueue(4)
print q.isEmpty()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print "Items"
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()


class MyDeque:
    def __init__(self):
        self.items = []
    def addFront(self, item):
        self.items.insert(0, item)
    def addRear(self, item):
        self.items.append(item)
    def removeFront(self):
        return self.items.pop(0)
    def removeRear(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def isEmpty(self):
        return len(self.items)==0
    def insertList(self, Lis):
        for element in Lis:
            self.items.append(element)
    def __str__(self):
        return "".join(self.items)

print "MyDeque Operations"
d=MyDeque()
print(d.isEmpty())
d.addRear(4)
d.addRear('dog')
d.addFront('cat')
d.addFront(True)
print(d.size())
print(d.isEmpty())
d.addRear(8.4)
print(d.removeRear())
print(d.removeFront())


# Singly Linked Lists
class Node:
    def __init__(self, dat):
        self.data = dat
        self.next = None
    def setData(self, dat):
        self.data = dat
    def getData(self):
        return self.data
    def setNext(self, nex):
        self.next = nex
    def getNext(self):
        return self.next

class UnorderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head==None
    def add(self, num):
        newNode = Node(num)
        temp = self.head
        newNode.setNext(self.head)
        self.head = newNode
    def size(self):
        count = 0
        current = self.head
        while current!=None:
            count = count + 1
            current = current.getNext()
        return count
    def find(self, num):
        current = self.head
        position = 0
        while current!=None:
            position = position + 1
            if current.getData()==num:
                return True, position
            current = current.getNext()
        return False, -1
    def remove(self, dat):
        currentNode = self.head
        previousNode = self.head
        while currentNode!=None:
            if currentNode.getData()==dat:
                break
            previousNode = currentNode
            currentNode = currentNode.getNext()
        if currentNode.getData()==dat:
            previousNode.setNext(currentNode.getNext())
            currentNode.setNext(None)
            return currentNode
        else:
            return "Element Not Found"
    def display(self):
        headNode = self.head
        currentNode = headNode
        while currentNode!=None:
            print currentNode.getData(), "->",
            currentNode = currentNode.getNext()

class OrderedList:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def add(self, num):
        if self.head==None:
            self.head = Node(num)
        else:
            currentNode = self.head
            previousNode = self.head
            while currentNode!=None:
                if num > currentNode.getData():
                    previousNode = currentNode
                    currentNode = currentNode.getNext()
                else:
                    break
            newNode = Node(num)
            newNode.setNext(currentNode)
            previousNode.setNext(newNode)
    def find(self, num):
        current = self.head
        position = 0
        while current!=None:
            position = position + 1
            if current.getData()==num:
                return True, position
            current = current.getNext()
        return False, -1
    def remove(self, dat):
        currentNode = self.head
        previousNode = self.head
        while currentNode!=None:
            if currentNode.getData()==dat:
                break
            previousNode = currentNode
            currentNode = currentNode.getNext()
        if currentNode.getData()==dat:
            previousNode.setNext(currentNode.getNext())
            currentNode.setNext(None)
            return currentNode
        else:
            return "Element Not Found"
    def display(self):
        headNode = self.head
        currentNode = headNode
        while currentNode!=None:
            print currentNode.getData(), "->",
            currentNode = currentNode.getNext()

class HashTable:

    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

# The collision resolution technique is linear probing with a plus 1 rehash function. The put function (see Listing 3)
# assumes that there will eventually be an empty slot unless the key is already present in the self.slots. It computes
# the original hash value and if that slot is not empty, iterates the rehash function until an empty slot occurs. If a
# nonempty slot already contains the key, the old data value is replaced with the new data value.
# One list, called slots, will hold the key items and a parallel list, called data, will hold the data values. When we look
# up a key, the corresponding position in the data list will hold the associated data value.

    def put(self, key, data):
        hashvalue = self.hashfunction(key, len(self.slots))
        if self.slots[hashvalue] == None: #if no such key exists!
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else:
                nextSlot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextSlot]!=None and self.slots[nextSlot]!=key:
                    nextSlot = self.rehash(nextSlot, len(self.slots))
                if self.slots[nextSlot]==None: # found a open slot
                    self.slots[nextSlot] = key
                    self.slots[nextSlot] = data
                else: # replace
                    self.data[nextSlot] = data

    def get(self, key):
        startSlot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startSlot
        while self.slots[position]!=None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position,len(self.slots))
                if position == startSlot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def hashfunction(self, key, size):
        return key%size

    def rehash(self, oldhash, size):
        return (oldhash+1)%size

#We stated earlier that in the best case hashing would provide a O(1), constant time search technique. However, due to collisions,
# the number of comparisons is typically not so simple. Even though a complete analysis of hashing is beyond the scope of this text,
# we can state some well-known results that approximate the number of comparisons necessary to search for an item.

#The most important piece of information we need to analyze the use of a hash table is the load factor. Conceptually, if lambda is small,
# then there is a lower chance of collisions, meaning that items are more likely to be in the slots where they belong.
# If lambda is large, meaning that the table is filling up, then there are more and more collisions. This means that collision
# resolution is more difficult, requiring more comparisons to find an empty slot. With chaining, increased collisions means an
# increased number of items on each chain.



# Binary Tree
class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def preorder(self):
        print(self.key)
        if self.leftChild:
            self.left.preorder()
        if self.rightChild:
            self.right.preorder()

class BinHeap:

    def __init__(self):
        self.heapList = [0]
        self.size = 0

    def insert(self, num):
        self.heapList.append(num)
        self.size = self.size + 1
        self.percolateUp(self.size)

    def percolateUp(self, i):
        while i//2 > 0 : # the parent of last node which was appended lies in n/2 where n is the total number of nodes
            if self.heapList[i] < self.heapList[i//2]:
                temp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = temp
            i = i // 2

    def delMin(self):
        retVal = self.heapList[1]
        self.heapList[1] = self.heapList[self.size]
        self.size = self.size - 1
        self.heapList.pop()
        self.percolateDown(1)
        return retVal

    def percolateDown(self, i):
        while (i * 2) <= self.size:
            mc = self.getMinChild(i) # get minimum of both child of i
            if self.heapList[mc] < self.heapList[i]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def getMinChild(self, i):
        if i * 2 + 1 > self.size: # of only left child exists
            return i * 2 # return index of left child
        else: # else return whichiver is minimum
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def buildHeap(self, alist):
        i = len(alist)//2
        self.size = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0: #only heapify the non child nodes
            self.percolateDown(i)
            i = i - 1


# A node of a trie
class TrieNode:

    def __init__(self, str):
        self.str = str
        self.dic = {}

    def getStr(self):
        return self.str

    def getDic(self):
        return self.dic

    def setNext(self, char ,aNode):
        self.dic[char] = aNode

    def getNext(self, char):
        if self.dic.has_key(char):
            return self.dic[char]

    def getString(self):
        resultString = self.str
        if(not self.dic.keys()):
            return resultString
        resultString=resultString + "\nConnected to: "
        for char in self.dic.keys():
            resultString = resultString + char + "\t"
        return resultString

class Trie:

    def __init__(self, words):
        self.startNode = TrieNode("")
        for word in words:
            currentNode = self.startNode
            for char in word:
                nextNode = currentNode.getNext(char)
                if (nextNode is None):
                    nextNode = TrieNode(currentNode.getString() + char)
                    currentNode.setNext(char, nextNode)
                    currentNode = nextNode



    def wordStartsWith(self,string):
        currNode=self.startNode
        for letter in string:
            if(not currNode.getNext(letter)):
                return False
            else:
                currNode=currNode.getNext(letter)
        return True
print "################################"

class MyTrieNode:

    def __init__(self, str):
        self.words = 0 # how many words in the dictionary are represented by that prefix
        self.prefixes = 0 # how many words have the prefix of the vertex
        self.str = str
        self.dic = {}
#wrapper
class MyTrie:
    missingNum = 1
    def addWord(self, word, currentNode):
        aNode = MyTrieNode('')
        if not word:
            currentNode.words = currentNode.words + 1
        else:
            currentNode.prefixes = currentNode.prefixes + 1
            k = word[:1]
            if not currentNode.dic.has_key(k):
                aNode.str = k
                currentNode.dic[k] = aNode
                currentNode = aNode
            else:
                currentNode = currentNode.dic[k]
            self.addWord(word[1:], currentNode)

    def countWords(self, word, currentNode):
        k = word[:1]
        if not k:
            return currentNode.words
        elif not currentNode.dic.has_key(k):
            return 0
        else:
            currentNode = currentNode.dic[k]
            return self.countWords(word[1:], currentNode)

    def countPrefixes(self, prefix, currentNode):
        k = prefix[:1]
        if not k:
            return currentNode.prefixes
        elif not currentNode.dic.has_key(k):
            return 0
        else:
            currentNode = currentNode.dic[k]
            return self.countPrefixes(prefix[1:], currentNode)

    def coutWordWithMissingWord(self, word, currentNode):
        k = word[:1]
        if not k:
            return currentNode.words
        elif not currentNode.dic.has_key(k) and self.missingNum == 1:
            print "todo"
            self.missingNum = 0
            #return max of all recursion
            max = 0
            for key in currentNode.dic:
                val = self.coutWordWithMissingWord(word, currentNode.dic[key])
                if val > max:
                    max = val
            return max
        elif currentNode.dic.has_key(k):
            currentNode = currentNode.dic[k]
            return self.coutWordWithMissingWord(word[1:], currentNode)
        else:
            return 0

    def countWords1(self, currentNode, word, missingLetters):
        k = word[:1]
        if not k:
            return currentNode.words
        elif not currentNode.dic.has_key(k) and missingLetters==0:
            return 0
        elif not currentNode.dic.has_key(k):
            currentNode = currentNode.dic[k]
            return self.countWords1(currentNode, word[1:], missingLetters-1)
        else:
            r = self.countWords1(currentNode, word, missingLetters - 1)
            currentNode = currentNode.dic[k]
            r = r + self.countWords1(currentNode, word[1:], missingLetters)
            return r

root = MyTrieNode('')
mytrie = MyTrie()
mytrie.addWord('shayan', root)
mytrie.addWord('shashi', root)
mytrie.addWord('shome', root)
print "shayan count words: ", mytrie.countWords('shayan', root)
print "shashi count words: ", mytrie.countWords('shashi', root)
print "shome count words: ", mytrie.countWords('shome', root)
print "sh prefix count: ", mytrie.countPrefixes('sh', root)
#print "shayn count words: ", mytrie.countWords1(root, 'shyan', 1)