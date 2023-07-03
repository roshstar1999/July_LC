class Solution:
    def __init__(self):
        self.ans=0

    def help(self,start,requests,indegree,count):
        

        if start==len(requests):
            for i in indegree:
                if i:
                    return
            self.ans=max(self.ans,count)
            return

        #in

        indegree[requests[start][0]]-=1
        indegree[requests[start][1]]+=1

        self.help(start+1,requests,indegree,count+1)

        #out
        indegree[requests[start][0]]+=1
        indegree[requests[start][1]]-=1

        self.help(start+1,requests,indegree,count)





    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        indegree=[0]*n

        self.help(0,requests,indegree,0)
        return self.ans

        

