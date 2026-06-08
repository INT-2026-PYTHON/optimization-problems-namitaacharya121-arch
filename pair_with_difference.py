def has_pair_brute(nums, k):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if abs(nums[i] - nums[j]) == k:
                return True
    return False


def has_pair_fast(nums, k):
    num_set = set(nums)

    for x in nums:
        if (x + k) in num_set or (x - k) in num_set:
            return True

    return False


nums = [1, 5, 3, 4, 2]
k = 3

print("Brute Force:", has_pair_brute(nums, k))
print("Optimized:  ", has_pair_fast(nums, k))