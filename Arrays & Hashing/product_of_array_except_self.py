class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prefix_prod =1
        postfix_prod=1
        res = [0]*n
        for i in range(n):
            res[i]= prefix_prod
            prefix_prod *= nums[i]
        for i in range(n-1,-1,-1):
            res[i]*=postfix_prod
            postfix_prod*=nums[i]
        return res
# arrr =[-1,1,0,-3,3]
# prod = 1
# for i in range(len(arrr)):
#     prod *=arrr[i]
# res = [prod//x for x in arrr if x>0]
# print(res)
