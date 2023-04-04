# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
# Input: arr = [1,2,2,1,1,3]
#Output: true
#Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        coccur ={}
        co =[]
        take=1
        for i in arr:
            if i not in coccur:
                coccur[i]=1
            else:
                coccur[i]+=1
        for a,b in coccur.items():
            co.append(b)
        for i in range(0,len(co)):
            for j in range(i+1,len(co)):                 
                if co[j]== co[i]:
                    take += 1
        if take>1:
            return False
        else:
            return True
        
  

