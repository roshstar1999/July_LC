def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
        for i in d.keys():
            if d[i]==1:
                return i
        return -1

#Bit Manipulation solution-->


class Solution:
   
    def singleNumber(self, nums: List[int]) -> int:
        ones=0
        twos=0

        for num in nums:
            ones=(ones^num) & ~twos
            twos=(twos^num) & ~ones

        return ones

