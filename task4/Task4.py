import sys

with open(sys.argv[1], 'r') as f:
    nums = [int(line) for line in f]

nums.sort()

median = nums[len(nums) // 2]

total_moves = sum(abs(num - median) for num in nums)

print(total_moves)
