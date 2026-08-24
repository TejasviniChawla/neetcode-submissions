class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mplr = 1
        arr =[]
        z = 0
        z_count =0

        for i in nums: 
            if i!=0:
                mplr*=i
            else: 
                z = 1 
                z_count += 1 
        
        if z_count > 1 :
            return [0]*len(nums)
        
        
        for i in nums: 
            if i!=0 and z==0: 
                arr.append(mplr//i)
            elif i!=0 and z==1:
                arr.append(0)
            elif i!=0 and z==0:
                arr.append(0)
            else: 
                arr.append(mplr)
        
        return arr



        