'''
Given two arrays, write a function to compute their intersection.
e.g.
(Input -> Output)  
nums1 = [1,2,2,1], nums2 = [2,2] -> [2]
nums1 = [4,9,5], nums2 = [9,4,9,8,4] -> [9,4]
'''
def intersection(nums1: list,nums2: list) -> list:
    Hash = dict()
    result = list()
    for x in nums1:
        Hash[x] = 1
    
    for x in nums2:
        if(x in Hash):
            result.append(x)                
            del Hash[x]
    return result

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersection(nums1,nums2))