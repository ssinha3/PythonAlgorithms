def sequentialSearch(testList, num):
    for x in testList:
        if x == num:
            return 'Found'
    return 'Not Found'

testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequentialSearch(testlist, 3))
print(sequentialSearch(testlist, 13))

def binarySearch(testList, num):
    mid = len(testList)//2
    if(len(testList)==0):
        return 'Not Found'
    elif testList[mid] == num:
        return 'Found'
    else:
        return binarySearch(testList[:mid-1], num)
        return binarySearch(testList[mid+1:], num)

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binarySearch(testlist, 3))
print(binarySearch(testlist, 13))


#Hashing http://interactivepython.org/courselib/static/pythonds/SortSearch/searching.html#hashing
#Given a collection of items, a hash function that maps each item into a unique slot is referred to as a perfect hash function.
# If we know the items and the collection will never change, then it is possible to construct a perfect hash function
# Unfortunately, given an arbitrary collection of items, there is no systematic way to construct a perfect hash function.
# One way to always have a perfect hash function is to increase the size of the hash table so that each possible value in
# the item range can be accommodated. This guarantees that each item will have a unique slot. Although this is practical for
# small numbers of items, it is not feasible when the number of possible items is large.

# Folding method :  constructing hash functions begins by dividing the item into equal-size pieces (the last piece may
# not be of equal size). These pieces are then added together to give the resulting hash value.
# If we assume our hash table has 11 slots, then we need to perform the extra step of dividing by 11 and keeping the remainder.

# Mid-square method : We first square the item, and then extract some portion of the resulting digits.By extracting
# the middle two digits, 93, and performing the remainder step

# Character Based :  We can also create hash functions for character-based items such as strings. The word cat can be thought
# of as a sequence of ordinal values. We can then take these three ordinal values, add them up, and use the
# remainder method to get a hash value. It is interesting to note that when using this hash function, anagrams will always
# be given the same hash value. To remedy this, we could use the position of the character as a weight.


#Collision Resolution:
#When two items hash to the same slot, we must have a systematic method for placing the second item in the hash table.
# This process is called collision resolution.

#open addressing : tries to find the next open slot or address in the hash table
 # Type 1  linear probing : By systematically visiting each slot one at a time, we are performing an open addressing
 # technique called linear probing.
 # Problem: A disadvantage to linear probing is the tendency for clustering; items become clustered in the table.
 # This means that if many collisions occur at the same hash value, a number of surrounding slots will be filled by the
 # linear probing resolution. This will have an impact on other items that are being inserted
 # Solution Rehashing 1: extend the linear probing technique so that instead of looking sequentially for the next open
 # slot, we skip slots, thereby more evenly distributing the items that have caused collisions. This will potentially
 # reduce the clustering that occurs.  plus 3 probe. This means that once a collision occurs, we will look at every
 # third slot until we find one that is empty
 # Solution Rehashing 2 quadratic probing: A variation of the linear probing idea is called quadratic probing. Instead
 # of using a constant skip value, we use a rehash function that increments the hash value by 1, 3, 5, 7, 9, and so on.
 # This means that if the first hash value is h, the successive values are h+1, h+4, h+9, h+16, and so on. In other words,
 # quadratic probing uses a skip consisting of successive perfect squares.
 # Solution 3: Chaining : Chaining allows many items to exist at the same location in the hash table. When collisions
 # happen, the item is still placed in the proper slot of the hash table. As more and more items hash to the same location,
 # the difficulty of searching for the item in the collection increases

 # Analysis of Hashing The most important piece of information we need to analyze the use of a hash table is the load factor,
 # lambda. Conceptually, if lambda is small, then there is a lower chance of collisions, meaning that items are more likely to be in
 # the slots where they belong. If lambda is large, meaning that the table is filling up, then there are more and more collisions.
 # This means that collision resolution is more difficult, requiring more comparisons to find an empty slot. With chaining,
 # increased collisions means an increased number of items on each chain.

from Basics import HashTable
H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
print(H[20])
print(H[17])
H[20]='duck'
print(H[20])
print(H[99])


# Insertion Sort
print "Insertion Sort"
def insertionSort(alist):
    for i in range(1, len(alist)):
        temp = alist[i]
        position = i-1;
        while(position>=0 and alist[position] > temp):
            alist[position+1] = alist[position]
            position = position - 1
        alist[position+1] = temp

alist = [54,26,93,17,77,31,44,55,20]
insertionSort(alist)
print(alist)

#Shell -Sort ToDo
def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for startposition in range(sublistcount):
        gapInsertionSort(alist, startposition, sublistcount)
      print("After increments of size",sublistcount, "The list is",alist)
      sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i
        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap
        alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print(alist)


# Merge Sort
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
        left = alist[:mid]
        right = alist[mid:]
        mergeSort(left)
        mergeSort(right)

        i=0
        j=0
        k=0

        while i< len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i = i + 1
            else:
                alist[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            alist[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            alist[k] = right[j]
            j = j + 1
            k = k + 1

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)


# Quick Sort
def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
    if first < last:
       splitpoint = partition(alist, first, last)
       quickSortHelper(alist, first, splitpoint - 1)
       quickSortHelper(alist, splitpoint + 1, last)

def partition(alist, first, last):
    pivotVal = alist[first]
    left = first + 1
    right = last
    done = False
    while not done:
        while alist[left] <= pivotVal and left <= right:
            left = left + 1
        while alist[right] >= pivotVal and right >= left:
            right = right - 1
        if right < left:
            done = True
        else:
            temp = alist[left]
            alist[left] = alist[right]
            alist[right] = temp
    temp = alist[first]
    alist[first] = alist[right]
    alist[right] = temp

    return right

alist = [54,26,93,17,77,31,44,55,20]
quickSort(alist)
print(alist)
