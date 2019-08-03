"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组,求出这个数组中的逆序对的总数P。并将P对1000000007取模的结果输出。 即输出P%1000000007
"""
class Solution1:
    def InversePairs(self, data):
        Sortdata = self.quick_sort(data)
        res = 0
        for i in Sortdata:
            res += data.index(i)
            data.pop(data.index(i))
        return res
	# 使用的快排
    def quick_sort(self, data):
        if len(data) < 2:
            return data
        left = self.quick_sort([i for i in data[1:] if i <= data[0]])
        right = self.quick_sort([j for j in data[1:] if j > data[0]])
        return left + [data[0]] + right
    """
    def quick_sort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less_than_pivot = [x for x in array if x <= pivot]
        more_than_pivot = [x for x in array if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(more_than_pivot)
    """

print(Solution1().quick_sort([1,2,3,2,1]))


#c风格快排
# 分组基准
# 对于上面的代码，分组基准的选取只是取列表的第一个值，太过于随便，当取到序列的中间值时，快排效率是最高的，
# 第一个值未必是列表的中间值。为了解决这个问题，我们可以选取列表中的几个值进行简单的比较，
# 然后取这几个值的中间值 作为分组基准。

# 空间使用大。
# 上面的代码已经解决了比较次数的问题。

# 若序列长度过于小(比如只有几个元素)，快排效率就不如插入排序了。
# 我们可以设置一个列表元素大小的临界值，若小于这个值，就用插入排序，大于这个值用快排。
def quick_sort(L):
    return q_sort(L, 0, len(L) - 1)

def q_sort(L, left, right):
    if left < right:
        pivot = Partition(L, left, right)

        q_sort(L, left, pivot - 1)
        q_sort(L, pivot + 1, right)
    return L

def Partition(L, left, right):
    pivotkey = L[left]

    while left < right:
        while left < right and L[right] >= pivotkey:
            right -= 1
        L[left] = L[right]
        while left < right and L[left] <= pivotkey:
            left += 1
        L[right] = L[left]

    L[left] = pivotkey
    return left

L = [5, 9, 1, 11, 6, 7, 2, 4]

print(quick_sort(L))