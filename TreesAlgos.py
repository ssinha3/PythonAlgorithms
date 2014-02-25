import operator
from Basics import BinaryTree
print ' TREE '
r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')
print(r.getRightChild())
print(r.getRightChild().getRootVal())
r.getRightChild().setRootVal('hello')
print(r.getRightChild().getRootVal())

print "************"
#Using the information from above we can define four rules as follows:
#If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.
#If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator represented
# by the current token. Add a new node as the right child of the current node and descend to the right child.
#If the current token is a number, set the root value of the current node to the number and return to the parent.
#If the current token is a ')', go to the parent of the current node.

#it is clear that we need to keep track of the current node as well as the parent of the current node. The tree interface
# provides us with a way to get children of a node, through the getLeftChild and getRightChild methods, but how can we keep
# track of the parent? A simple solution to keeping track of parents as we traverse the tree is to use a stack. Whenever we
# want to descend to a child of the current node, we first push the current node on the stack. When we want to return to the
# parent of the current node, we pop the parent off the stack.
from Basics import MyStack
#Parse Tree
def buildParseTree(inputString):
    st = MyStack() # to keep track of parent
    tr = BinaryTree('') #create a empty node
    currentTree = tr # make it current Node
    st.push(tr) # push it into stack
    lis = inputString.split()
    for element in lis:
        if element == '(':
            currentTree.insertLeft('') #insert a new left node
            st.push(currentTree) # push the parent
            currentTree = currentTree.getLeftChild() # traverse left
        elif element not in ['+', '-', '*', '/', ')']: # its a number
            currentTree.setRootVal(int(element))
            parent = st.pop()
            currentTree = parent
        elif element in ['+', '-', '*', '/']: #its a operator
            currentTree.setRootVal(element)
            currentTree.insertRight('')
            st.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif element in ')':
            currentTree = st.pop()
        else:
            print 'value error'
    return tr


def eval(tree):
    opr = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    left = tree.getLeftChild()
    right = tree.getRightChild()
    if left and right:
        func = opr[tree.getRootVal()]
        return func(eval(left), eval(right))
    else:
        return tree.getRootVal()

def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

def postordereval(tree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
    res1 = None
    res2 = None
    if tree:
        res1 = postordereval(tree.getLeftChild())
        res2 = postordereval(tree.getRightChild())
        if res1 and res2:
            return opers[tree.getRootVal()](res1,res2)
        else:
            return tree.getRootVal()

def inorder(tree):
  if tree != None:
      inorder(tree.getLeftChild())
      print(tree.getRootVal())
      inorder(tree.getRightChild())

def printexp(tree): #inorder
  sVal = ""
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal

pt = buildParseTree("( ( 10 + 5 ) * 3 )")
postorder(pt)
print "value, ",eval(pt)
print "value postorder, ",postorder(pt)
print "value preorder, ",preorder(pt)
print "value postordereval, ",postordereval(pt)
print "value inorder, ",inorder(pt)
print "value printexp, ",printexp(pt)
