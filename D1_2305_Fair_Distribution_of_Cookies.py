class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:

        def solve(i,arr):
            if i==n:
                nonlocal ans
                mx=max(arr)
                ans=min(ans,mx)
                return

            for j in range(k):
                arr[j]+=cookies[i]
                solve(i+1,arr)
                arr[j]-=cookies[i]
                if arr[j]==0:
                    break
        n=len(cookies)
        ans=float('inf')
        arr=[0]*k
        solve(0,arr)
        return ans

                

            
