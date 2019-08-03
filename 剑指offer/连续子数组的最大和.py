"""
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。
,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。
但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？
例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。
给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)



本题可以用简单的动态规划完成，用f(i)f(i)记录以a[i]为结尾的子数组的最大和，
如果前面i-1的子数组的最大和为负值，那么全部抛弃，f(i)f(i)就等于当前数组值。
同时用res维护得到的数组最大和的最大值，有以下关系：
f(0)=a[0]f(0)=a[0]
f(1)=max(f(0)+a[1],a[1])f(1)=max(f(0)+a[1],a[1])
……
f(i)=max(f(i−1)+a[i−1],a[i])
"""


class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        maxsum = array[0]
        res = maxsum
        for i in range(1, len(array)):
            maxsum = max(maxsum + array[i], array[i])
            res = max(maxsum, res)
        return res


print(Solution().FindGreatestSumOfSubArray([1, -2, 3, 10, -4, 7, 2, -5]))



def quick_sort_senior(array):
    return quick_sort_junior(array,0,len(array)-1)

def quick_sort_junior(array, left, right):
    if left<right:
        piv = sub_sort(array, left, right)
        quick_sort_junior(array, left, piv-1)
        quick_sort_junior(array, piv + 1, right)
    return array


def sub_sort(array, left, rignt):
    piv = array[left]
    while left < rignt:
        while left < rignt and array[rignt] > piv:
            rignt -= 1
        array[left] = array[rignt]
        while left < rignt and array[left] < piv:
            left += 1
        array[rignt] = array[left]
    array[left] = piv
    return left


print(quick_sort_senior([1, -2, 3, 10, -4, 7, 2, -5]))
