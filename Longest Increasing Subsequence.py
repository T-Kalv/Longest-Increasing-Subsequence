"""
Longest Increasing Subsequence

You are given an array of integers. Return the length of the longest increasing subsquence (does not have to be necessarily contiguous) in the array.

E.g. [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
The following input should return 6.
"""
def subsequence(arr):
  if not arr:
    return 0
  cache = [1] * len(arr)
  for i in range(1, len(arr)):
      for j in range(i):
        if arr[i] > arr[j]:
            cache[i] = max(cache[i], cache[j] + 1)
  print(cache)
  return max(cache)

print(subsequence([0, 7, 3, 15, 2, 10, 9, 18, 1, 13, 5, 23, 25, 19, 17, 55]))

