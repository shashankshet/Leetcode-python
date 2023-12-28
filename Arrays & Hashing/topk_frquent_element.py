class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums)==1:
            return nums
        mp = {}
        for i in nums:
            if i in mp:
                mp[i]+=1
            else:
                mp[i]=1
        sorted_res = sorted(mp.items(), key=lambda x: x[1], reverse=True)

        res = []
        for i in range(k):
            res.append(sorted_res[i][0])

        return res
