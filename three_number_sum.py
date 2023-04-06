# def threeNumberSum(array, targetSum):
#     array.sort()
#     res = []
    
#     for i in range(len(array)):
#         twoSum(array, i, res, targetSum)
#     return res

# def twoSum(array, i, res, targetSum):
#     l, r = i + 1, len(array) - 1

#     while l < r:
#         if array[i] + array[l] + array[r] < targetSum:
#             l += 1
#         elif array[i] + array[l] + array[r] > targetSum:
#             r -= 1
#         else:
#             res.append([array[i], array[l], array[r]])
#             l += 1
#     return res

# def threeNumberSum(array, targetSum):
#     foundTriplets = []
#     itemMap = {}
#     array.sort()

#     for i in array:
#         itemMap[i] = True

#     for i in array:
#         for j in array:
#             if i != j:
#                 targetSumDelta = targetSum - (i + j)
#                 if targetSum != i and targetSumDelta != j and targetSumDelta in itemMap:
#                     hit = [i, j, targetSumDelta]
#                     hit.sort()
#                     if not hit in foundTriplets:
#                         foundTriplets.append(hit)

#     return foundTriplets

def threeNumberSum(array, targetSum):
    lst = []
    for num1 in array:
        for num2 in array[array.index(num1) + 1:]:
            if (targetSum - num1 - num2) in array[array.index(num2) + 1:]:
                lst.append(sorted([num1, num2, targetSum - num1 - num2]))
    return sorted(lst)