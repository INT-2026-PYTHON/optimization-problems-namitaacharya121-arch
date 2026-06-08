def count_pairs_brute(nums, target):
    count = 0

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                count += 1

    return count


def count_pairs_fast(nums, target):
    freq = {}
    count = 0

    for x in nums:
        complement = target - x

        if complement in freq:
            count += freq[complement]

        freq[x] = freq.get(x, 0) + 1

    return count


nums = [1, 5, 7, -1, 5]
target = 6

print("Brute Force:", count_pairs_brute(nums, target))
print("Optimized:  ", count_pairs_fast(nums, target))