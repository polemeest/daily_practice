nums, target = [2,7,11,15], 9
lst = [[[i, j] for j in range((i + 1) % len(nums), len(nums)) if nums[i] + nums[j] == target] for i in range(len(nums))]

# for i in range(len(nums)):
#     for j in range((i + 1) % len(nums), len(nums)):
#         if nums[i] + nums[j] == target:
#             lst.append([i,j])
#             break
print(lst[0][0])
