def iterative_binary_search(sorted_list, target):
    (left, right) = (0, len(sorted_list) - 1)
    counter = 0

    while left <= right:
        counter += 1

        mid = (left + right) // 2

        if target < sorted_list[mid]:
            right = mid - 1
            continue
        elif target > sorted_list[mid]:
            left = mid + 1
            continue

        return mid, counter

    return -1, counter


# def recursive_binary_search(sorted_list, left, right, target):
#
#     # Base condition
#     if left > right:
#         return -1
# 
#     mid = (left + right) // 2
#
#     if target == sorted_list[mid]:
#         return mid
#     elif target < sorted_list[mid]:
#         return recursive_binary_search(sorted_list, left, mid - 1, target)
#     else:
#         return recursive_binary_search(sorted_list, mid + 1, right, target)


nums = [num for num in range(1000)]
num = 0

index, count = iterative_binary_search(nums, num)
# index = recursive_binary_search(nums, 0, len(nums)-1, num)

if index > -1:
    print(f"Element found at index: {index}")
    print(f"Iterations: {count}")
else:
    print("Element found not in the list")
    print(f"Iterations: {count}")