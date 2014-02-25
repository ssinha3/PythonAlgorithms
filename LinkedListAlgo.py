from Basics import Node
from Basics import UnorderedList
from Basics import OrderedList
print "Linked List!"
myLL = UnorderedList()
myLL.add(1)
myLL.add(2)
myLL.add(3)
myLL.add(4)
myLL.add(5)
# 5->4->3->2->1
x, y = myLL.find(2)
print x, y
myLL.remove(4)
myLL.display()
print ""
print "Ordered List"
myOLL = OrderedList()
myOLL.add(1)
myOLL.add(2)
myOLL.add(3)
myOLL.add(4)
myOLL.add(5)
myOLL.display()