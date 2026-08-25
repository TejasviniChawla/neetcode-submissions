class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # to find: nums[i]+nums[j] = -nums[k]
        # [-1,0,1,2,-1,-4]
        # -4,-1,-1, 0, 1, 2

        nums.sort()
        ans = []
        print(nums)
        count = 0

        for i in range(0, len(nums)-2): 

            if (i!=0 and nums[i]==nums[i-1]):
                 continue
            else: 

                target= -1*nums[i]
                l, r = i+1, len(nums)-1

                while l<r and i<l<r<=len(nums)-1: 
                    temp = nums[l]+nums[r]
                    if temp<target: 
                        l+=1
                    elif temp>target: 
                        r-=1
                    else: 
                        ans.append([nums[i], nums[l], nums[r]])
                        count +=1
                        l+=1
                        r-=1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        return ans



        