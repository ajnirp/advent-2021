from math import floor, ceil

with open('7.txt') as f:
    nums = [int(x) for x in f.read().strip().split(',')]

def median(nums):
    nums.sort()
    length = len(nums)
    result = nums[length>>1]
    if length & 1 == 0:
        result += nums[(length>>1)-1]
        result >>= 1
    return result

def cost_absolute_deviations(nums, m):
    return sum(abs(x-m) for x in nums)

def cost_median(nums):
    return cost_absolute_deviations(nums, median(nums))

# median minimizes the sum of absolute deviations
print(cost_median(nums))

def mean(nums):
    return sum(nums) / len(nums)

def triangular(n):
    return (n*(n+1))//2

def cost_triangular_deviations(nums, m):
    return sum(triangular(abs(x-m)) for x in nums)

def brute_force(nums):
    min_, max_ = min(nums), max(nums)
    return min(cost_triangular_deviations(nums, i) for i in range(min_, max_+1))

# return the cost for both floor and ceil of mean
def cost_either_side_mean(nums):
    m = mean(nums)
    return cost_triangular_deviations(nums, floor(m)), \
           cost_triangular_deviations(nums, ceil(m))

# this certainly works but is a slow way to do things in general
# print(brute_force(nums))

# this also certainly works but is quicker than brute force b/c we check only
# two values
# reasoning: mean minimizes the sum of squared errors
# What we have here is not squaring but triangular numbers. So we check on both
# sides of the mean to be sure. Rounding the mean to the closest integer might
# not work
print(min(cost_either_side_mean(nums)))
