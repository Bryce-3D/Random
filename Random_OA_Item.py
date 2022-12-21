#This was my solution to a random online assessment item I saw in a 
#discord server on 2022-09-04

'''Online Assessment Item
Given an array of strings, your task is to find the number of pairs which one 
is a suffix of other string (or equal).

Example:
    arr = ["cba", "a", "a","b", "ba", "ca"]
    Expected output = 8
        [cba, a] 
        [cba, a]
        [a, a] 
        [ba, a] 
        [ca, a]
        [cba, ba]
        [a, ba]
        [a, ca]
'''

'''Sketch of Algorithm
First reverse all the strings to convert it to a number of """prefix pairs""" 
problem Then sort the array alphabetically. Call this sorted array `l_sorted`.
In one pass of `l_sorted`, do the ff
- Create a dict `count` such that `count[s]` returns the number of instances 
  of string `s` in `l_s` (also doubles as a set to quickly check if a string 
  exists). Also add the empty string in it.
- Create a new list `l_s` which is just `l_sorted` but with dupes removed, 
  and with the empty string as the first element.

Create a new array `n_pairs` such that `n_pairs[i]` will return the number of 
strings which are a prefix of `l_s`, including `l_s` itself (even the same 
copy) and counting dupes.
Initialize the `n_pairs[0]=0` (the empty substring doesn't have a prefix in `l_s`)
Then linearly scan `l_s` and do the ff (`i in range(1,len(l_s))`)
- Let `s = l_s[i]`. Let `l` be the length of `s`.
- Check all `l` prefixes excluding itself and including the empty string from 
  longest to shortest (`s[:-1:]` to `s[:-l:]`) Stop when you find the first 
  instance that exists in `count` (must eventually happen since the empty string 
  is guaranteed to be in `count`). Suppose that this string is `s_pre` (Another 
  option here is to instead trace `l_s` backwards to find the longest existing 
  strict prefix. Tracing the individual string's prefixes would surely be faster 
  tho if the max length of the string is given a low bound which I think is more 
  likely)
- Set `n_pairs[i]` to be `n_pairs[s_pre] + count[s]`. This is because prefixing 
  is transitive (a is prefix of b and b is prefix of c imply that a is prefix of 
  c), so `s` can either be paired with either itself or something that must be 
  a prefix of the longest prefix of `s` that exists. (Concrete example: 
  [a,abcd,ab,ab]. the prefixes of abcd within the list are either abcd itself or 
  something that is a prefix of ab since abc doesn't exist)
- Due to the list being sorted, the longest strict prefix must've been already 
  processed at this point so this algorithm should run fine.

Afterwards, add up all the entries and subtract it by `len(l_s)-1` since we 
don't count pairing an element with itself
'''

'''Time Complexity
I think the time complexity for this is `O(wnlogn + w^2n)` where 
`n`=number of strings, `w`=length of longest string

Reverse: `O(n)` words, `O(w)` each word
Sort: `O(nlogn)` comparisons, each of which is `O(w)`
build `count` and `l_s`: `O(n)`
Iterate through `l_s`:  `O(n)` words to iterate through, each takes at most 
    `O(w^2)` time to generate the at most `w` prefixes to check (assuming a good 
    hash, `in count` is `O(1)`)
adding the final tally: `O(n)` (assuming a good hash again)

If `w` is given some low bound like `w <= 20`, then it's practically `O(nlogn)`
'''

def numPairs(arr):
    arr = [i[::-1] for i in arr]   #Reverse all the strings given
    arr.sort()                     #Sort the elements alphabetically

    count = {'':0}
    l_s = ['']

    for s in arr:
        if s == l_s[-1]:    #Same as prev string
            count[s] += 1   #Increase count
        else:               #If new string
            count[s] = 1    #Start counting
            l_s.append(s)   #Update prev
    
    n_pairs = {'':0}
    for i in range(1,len()):
        s = l_s[i]   #Next string to check
        l = len(s)
        for j in range(1,l+1):
            if s[:-j:] in count:   #If prefix is found
                s_pre = s[:-j:]
                break
        n_pairs[s] = n_pairs[s_pre] + count[s]   #Number of shorter prefixes + number of dupes
    
    ans = 0
    for s in n_pairs:
        ans += n_pairs[s]   #Add all the counts
    ans -= len(n_pairs)-1   #Remove pairings with itself

    print(ans)

print(numPairs(["cba", "a", "a","b", "ba", "ca"]))
