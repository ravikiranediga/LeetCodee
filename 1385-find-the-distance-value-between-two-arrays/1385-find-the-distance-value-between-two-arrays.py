from bisect import bisect_left

class Solution:
    def findTheDistanceValue(self, arr1, arr2, d):

        arr2.sort()
        count = 0

        for num in arr1:
            i = bisect_left(arr2, num)

            valid = True

            if i < len(arr2) and arr2[i] - num <= d:
                valid = False

            if i > 0 and num - arr2[i - 1] <= d:
                valid = False

            if valid:
                count += 1

        return count