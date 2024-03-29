
# Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
# and each integer appears once or twice, return an array of all the integers that appears twice.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup ={}
        lst=[]
        for i in nums:
            if i not in dup:
                dup[i]= 1
            else:
                dup[i]+= 1
        for a,b in dup.items():
            if b==2:
                lst.append(a)
        return lst
