# Time Complexity : O(n)
# Space Complexity :O(1)
# Passed on Leetcode: yes

class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        def helper(target, tops, bottoms):
            bRot, tRot = 0, 0
            for i in range(len(tops)):
                if tops[i] != target and bottoms[i] != target:
                    return -1
                if tops[i] != target and bottoms[i] == target:
                    bRot += 1
                if bottoms[i] != target and tops[i] == target:
                    tRot += 1
            return min(bRot, tRot)

        rot = helper(tops[0], tops, bottoms)
        if rot == -1:
            return helper(bottoms[0], tops, bottoms) 
        return rot