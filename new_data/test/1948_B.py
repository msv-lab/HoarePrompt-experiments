import sys
from typing import List


def is_sorted(nums: List[int]):
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


def get_unsorted_idx(nums: List[int]):
    unsorted_idx = []
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            unsorted_idx.append(i)

    return unsorted_idx


def fix(nums: List[int], idx: int):
    num_to_fix = nums.pop(idx)
    split_nums = [int(x) for x in str(num_to_fix)]
    # [nums.insert(idx, num) for num in split_nums]
    split_nums.reverse()
    for num in split_nums:
        nums.insert(idx, num)

    return len(split_nums) - 1


lines = []
line_idx = 0
for line in sys.stdin:
    if line_idx % 2 == 0:
        lines.append(line)
    line_idx += 1
    if line_idx == (1 + 2 * 7) and len(line.split()) > 15:
        print(line)

lines.pop(0)

for test in lines:
    nums = [int(x) for x in test.strip().split()]
    if is_sorted(nums):
        print("yes")
        continue

    became_sorted = False
    continue_sorting = True
    while continue_sorting:
        unsorted_idx = get_unsorted_idx(nums)
        nums_inserted = 0
        for idx in unsorted_idx:
            if nums[idx] < 10:
                continue_sorting = False  # unsortable
            nums_inserted += fix(nums, idx + nums_inserted)
            if is_sorted(nums):
                became_sorted = True
                continue_sorting = False
                break

    if became_sorted:
        print("yes")
        continue
    print("no")
