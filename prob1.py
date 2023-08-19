# Time Complexity : O(nlogk)
# Space Complexity :O(1)
# Passed on Leetcode: yes

from bisect import bisect_left

def shortestWay(source, target):
    hashmap = {}
    for i in range(len(source)):
        if source[i] not in hashmap:
            hashmap[source[i]] = [i]
        else:
            hashmap[source[i]].append(i)

    tl = len(target)
    sl = len(source)
    sp, tp, count = 0, 0, 1  # Initialize count to 1
    while tp < tl:
        tChar = target[tp]  # Get the current character from the target
        if tChar not in hashmap:
            return -1
        
        res = bisect_left(hashmap[tChar], sp)
        
        if res >= sl:
            sp = 0
            count += 1

        if res == sl-1:
            tp += 1
            sp = 0

        else:
            sp = sp + 1  # Move sp one position to the right
            tp += 1

    return count

source = "abc"
target = "abcbc"
print(shortestWay(source, target))
