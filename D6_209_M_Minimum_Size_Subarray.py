def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        summ=0

        start=0
        
        minlen=10**5+1
        
        for i in range(len(nums)):
            summ+=nums[i]
            while (summ>=target):
                if (i-start+1<minlen):
                    minlen=i-start+1
                summ-=nums[start]
                start+=1
        if minlen==10**5+1:return 0
        else: return minlen
