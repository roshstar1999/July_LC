class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        count=0



        #if 2 strings are same, then atleast one of the chars needs to appear more than once so swap is possible
        if s==goal:
            n={}
            for i in s:
                if i in n:
                    n[i]+=1
                else:
                    n[i]=1

            for x in n.keys():
                if n[x]>1:
                    return True
            return False
            

        #for different ones first checking if >2 chars are diff, if yes cant swap
        p=[-1,-1]

        for i in range(len(s)):
            
            if s[i]!=goal[i]:
                if count<2:
                    p[count]=i
                count+=1
            
            #if more than 2 indexes having different chars, cant swap
            if count>2:
                return False
            
        if count<2:
            return False
    
        
        if s[p[1]]==goal[p[0]] and s[p[0]]==goal[p[1]]:
            return True
        else:
            return False
