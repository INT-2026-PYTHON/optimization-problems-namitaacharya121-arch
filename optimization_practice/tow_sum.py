def two_sum_brute(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return (i, j)


def two_sum_fast(nums, target):
    num_dict = {}

    for i in range(len(nums)):
        complement = target - nums[i]

        if complement in num_dict:
            return (num_dict[complement], i)

        num_dict[nums[i]] = i


nums = [2, 7, 11, 15]
target = 9

print("Brute Force:", two_sum_brute(nums, target))
print("Optimized:  ", two_sum_fast(nums, target))
print("Brute Force Time Complexity: O(n^2)")
print("Optimized Time Complexity:   O(n)")