"""
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length.
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Clarification:
Confused why the returned value is an integer but your answer is an array?
Note that the input array is passed in by reference, which means a modification to the input array will be known to the caller as well.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2]
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. 
It doesn't matter what you leave beyond the returned length.
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4]
Explanation: Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively. 
It doesn't matter what values are set beyond the returned length.
"""

# Time: O(n)
# Space: O(1)
def removeDuplicatesPythonic(nums):
    # The pythonic way would be to convert to a set and return len of that
    return len(set(nums))


# Time: O(n)
# Space: O(1)
def removeDuplicates(nums):
    if not nums:
        return 0

    index = 0
    while index <= (len(nums) - 2):
        if nums[index + 1] <= nums[index]:
            nums.pop(index + 1)
            continue

        index += 1
    return len(nums)
        



print(removeDuplicates([1,1,2])) # 2
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5
print(removeDuplicates([0,0,1,1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,9,10,10,10,10,10,10,11,11,11,11,11,12,12,12,12,12,13,13])) # 14
print(removeDuplicates([5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,31,31,31,31,31,31,31,31,31,31,31,31,31,150,150,150,151])) # 4

