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
