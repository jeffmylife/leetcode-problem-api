class Solution:

    def _flatten(self, nested_nums):
        if any(isinstance(el, list) for el in nested_nums):
            prefix = nested_nums[0]
            unpacked = nested_nums[1:]
            


    
    def _permute(self, nums):
        if len(nums) > 2: 
            tmp_lol = []
            loop_nums = list(nums)
            for i, _ in enumerate(loop_nums):
                # print("looping on i=%d el=%d"%(i, el))
                tmp_nums = [nums[i]] + nums[:i] + nums[i + 1:] 
                tmp_lol.append(tmp_nums)
                
                # will have permutations missing first el from tmp_nums
                sub_perms = Solution._permute(self, nums[:i] + nums[i + 1:])
                # add back first el to each 
                tmp_nums_r = [nums[i] , *sub_perms]
                # for j in sub_perms:
                #     if isinstance(j,list):
                #         print(*j)
                #         for k in j:
                #             if isinstance(k, list):
                #                 print(*k)

                tmp_lol.append(tmp_nums_r)
            return tmp_lol
        elif len(nums) == 2:
            return [nums[1], nums[0]]
        else:
            raise Exception("Major error")
    
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = Solution._permute(self,nums)
        
        print(permutations)
        return permutations
        
            
