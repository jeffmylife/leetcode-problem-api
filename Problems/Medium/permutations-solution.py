class Solution:

    def _flatten(lol):
        if all(isinstance(i, int) for i in lol) or all(isinstance(v, int) for l in lol for v in l):
            if len(lol) == 1: 
                return lol[0]
            return lol
        elif any(isinstance(i, list) for i in lol):
            ret = []
            for l in lol: 
                if isinstance(l, list) and  all(isinstance(i, int) for i in l):
                    f = Solution._flatten(l)
                    ret += [f]
                else: 
                    ret += l
            return ret
        else:
            return lol

    def _unique(lol):
        if isinstance(lol, list):
            return [list(x) for x in set(tuple(x) for x in lol)]
        else:
            return lol 
    
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

                
                print("current = " + str(nums[i]))
                print("sub_perm = " + str(sub_perms))
                # add back first el to each 
                # tmp_nums_r = [nums[i] , *sub_perms]
                if any(isinstance(el, list) for el in sub_perms):
                    prefix = nums[i]
                    assert isinstance(prefix, int), f"prefix = {prefix}"
                    to_map = [unpacked[0] if len(unpacked)==1 else unpacked for unpacked in sub_perms]
                    print("to map : " + str(to_map))
                    print()
                    triplets = list(map(lambda x: [prefix, *x], to_map))
                    
                    tmp_nums_r = triplets
                else: 
                    tmp_nums_r = [nums[i], *sub_perms]

                print(tmp_nums_r,end="\n\n\n")

                tmp_lol.append(tmp_nums_r)
            return tmp_lol
        
        elif len(nums) == 2:
            return [nums[1], nums[0]]
        elif len(nums) == 1: 
            return nums
        else:
            raise Exception("Major error")
    
    
    def permute(self, nums: List[int]) -> List[List[int]]:
        permutations = Solution._permute(self,nums)
        
        # print("\n\n".join([str(i) if len(i)==5 else str(str(i).replace("],","],\n")) + "\n\t\tlen= " + str(len(i)) for i in permutations] ))
        
        return Solution._unique(Solution._flatten(permutations))
        
            
