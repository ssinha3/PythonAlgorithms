# func(input 1(options), input 2(value,things to minimize) )
# worstCaseValue = defaultValue.
# check for base case.
# for all valid values in range input1(options)
# recursive formula of DP
# check and update worstCaseVal if better solution is found
# return the worst case value.
knownResults = dict()

def recMC(conValueList, changeVal):
    worstCaseValue = changeVal
    if changeVal in conValueList:
        knownResults[changeVal] = 1 # memoization
        return 1
    elif knownResults.has_key(changeVal): # return value which is memoized(i.e. if its saved in any previous recursive calls)
        return knownResults[changeVal]
    else:
        for i in [c for c in conValueList if c<=changeVal]:
            numCoins = 1 + recMC(conValueList, changeVal - i)
            if numCoins < worstCaseValue:
                worstCaseValue = numCoins
                knownResults[changeVal] = numCoins #memoization
    return worstCaseValue
#print(recMC([1,5,10,21,25],63))

# But the above approach is highly inefficient exponential, since we are repeating calculations to known solutions.
# We should save the results i.e. memoize the results.

# But Still its not ab DP solutions, since memoization is a just a part of DP.
#A truly dynamic programming algorithm will take a more systematic approach to the problem. Our dynamic programming solution
# is going to start with making change for one cent and systematically work its way up to the amount of change we require.
# This guarantees us that at each step of the algorithm we already know the minimum number of coins needed to make change for
# any smaller amount.
# dynamic programming algorithm to solve our change-making problem. dpMakeChange takes three parameters: a list of valid coin values,
# the amount of change we want to make, and a list of the minimum number of coins needed to make each value. When the function is done
# minCoins will contain the solution for all values from 0 to the value of change.

#DP
amnt = 63
minCoins = [0]*(amnt+1)
coinsUsed = [0]*(amnt+1)

def recMCDP(conValueList, changeVal, minCoins):
    for cents in range(changeVal+1):
        worstCaseCoinCount = cents
        newCoin = 1
        for j in [c for c in conValueList if c <= cents]:
            if minCoins[cents-j] + 1 < worstCaseCoinCount:
                worstCaseCoinCount = minCoins[cents-j]+1
                newCoin = j
        minCoins[cents] = worstCaseCoinCount
        coinsUsed[cents] = newCoin
    return minCoins[changeVal]

def printCoins(coinsUsed,change):
   coin = change
   while coin > 0:
      thisCoin = coinsUsed[coin]
      print(thisCoin)
      coin = coin - thisCoin


print(recMCDP([1,5,10,21,25],63, minCoins))
printCoins(coinsUsed,amnt)
print(coinsUsed)


#Given a list of N coins, their values (V1, V2, ... , VN), and the total sum S. Find the minimum number of coins the sum
# of which is S (we can use as many coins of one type as we want), or report that it's not possible to select coins in
# such a way that they sum up to S.
print "###############################################"
print "DP coin count problem!"
min = [999]*70
change = [999]*70
min[0] = 0
change[0] = 1
v = [1, 5, 10, 21, 25]
for i in range(1,66): # solution range 1 - 11
    for j in range(0,5): # range of denomination of coins, for all options or denominations
        if(v[j] <= i and min[i-v[j]] + 1 < min[i]): # for all denominations less than current sum,
            min[i] = min[i-v[j]] + 1
            change[i] = v[j]
print min
print change


print "DP for max increasing sequence!"
inp = [5, 3, 4, 8, 6, 7, 9, 10, 1, 2, 3, 4, 5] #input sequence
len_of_longest_inc_seq = [0]*len(inp) # storage of longest sequences found thus far
len_of_longest_inc_seq[0] = 1 # longest seq for length 1 is 1
current_max = len_of_longest_inc_seq[0] # initialized to 1
for i in range(0, len(inp)-1):
    if inp[i] <= inp[i+1]:
        current_max += 1
    else:
        current_max = 1
    if current_max > len_of_longest_inc_seq[i]: #should run always
        len_of_longest_inc_seq[i+1] = len_of_longest_inc_seq[i] + 1
    else:
        len_of_longest_inc_seq[i+1] = len_of_longest_inc_seq[i]
print len_of_longest_inc_seq[len(len_of_longest_inc_seq)-1]
print len_of_longest_inc_seq


# Zig-Zag http://community.topcoder.com/stat?c=problem_statement&pm=1259&rd=4493
# zigzag = [1, 7, 4, 9, 2, 5]
zigzag = [1, 17, 10, 13, 10, 16, 8]
longest_zig_zag_seq = [1]*len(zigzag)
current_max = 1
for i in range(0, len(zigzag)-2):
    if ((zigzag[i+1] - zigzag[i])/abs(zigzag[i+1] - zigzag[i])) != ((zigzag[i+2] - zigzag[i+1])/abs(zigzag[i+2] - zigzag[i+1])):
        current_max += 1
    else:
        current_max = 1
    if current_max > longest_zig_zag_seq[i+1]: #should run always
        longest_zig_zag_seq[i+2] = longest_zig_zag_seq[i+1] + 1
    else:
        longest_zig_zag_seq[i+2] = longest_zig_zag_seq[i+1]
print longest_zig_zag_seq
print longest_zig_zag_seq[len(longest_zig_zag_seq)-1]+1

print "Bad Neighbours!"
# Bad Neighbors http://apps.topcoder.com/forums/?module=Thread&threadID=707599&start=0&mc=4#1533461
#import math
donation = [10, 3, 2, 5, 7, 8]
def maxDonations(donation):
    dp1 = [0]*len(donation)
    dp2 = [0]*len(donation)
    if len(donation) < 1:
        return 0
    if len(donation) == 1:
        return donation[0]
    if len(donation) == 2:
        return max(donation[0], donation[1])
    if len(donation) == 3:
        return max(donation[0], donation[1], donation[2])
    dp1[0] = donation[0]
    dp1[1] = donation[0]
    for i in range(2, len(donation)):
        dp1[i] = max(dp1[i-2]+donation[i], dp1[i-1])
    dp2[0] = donation[1]
    dp2[1] = donation[1]
    for i in range(2, len(donation)):
        dp2[i] = max(dp2[i-2]+donation[i], dp2[i-1])

    print dp1
    print dp2
    print max(dp1[len(dp1)-2], dp2[len(dp2)-2])

maxDonations(donation)