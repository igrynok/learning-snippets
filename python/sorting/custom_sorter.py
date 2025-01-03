from collections import Counter

nums = [1, 1, 2, 2, 2, 3, 4, 4]
print(f'nums:{nums}')

# sort by frequency and in decreasing order if frequencies are the same
counter = Counter(nums)
sorted_nums = sorted(nums, key=lambda x: (counter[x], -x))
print(f'sorted nums:{sorted_nums}')
