def first_repeating_brute(nums):
    for j in range(len(nums)):
        for i in range(j):
            if nums[i] == nums[j]:
                return nums[j]
    return -1


def first_repeating_fast(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return num
        seen.add(num)

    return -1


nums = [10, 5, 3, 4, 3, 5, 6]

print("Brute Force:", first_repeating_brute(nums))
print("Optimized:  ", first_repeating_fast(nums))