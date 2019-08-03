"""
求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？
为此他特别数了一下1~13中包含1的数字有1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。
ACMer希望你们帮帮他,并把问题更加普遍化,
可以很快的求出任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。


输入：101314
当前位：1
高位（比十位高的数字）：1013
低位（比十位低的数字）：4

对于低位来说，
十位出现1的有101310, 101311，101312, 101313, 101314这5个数字

对于高位来说，
10～100的有10, 11, 12, 13, 14, 15, 16, 17, 18, 19这10个数字
101~200的有110, 111, 112, 113, 114, 115, 116, 117, 118, 119这10个数字
十位出现1在10~101300中有1013 × 10 = 10130个数字（理解了这个，后面就非常好理解了）

所以高位+低位有10135个数字

"""
# -*- coding:utf-8 -*-
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n <= 0:
            return 0

        # 定义算子
        operator = 1
        count = 0

        while n // operator:
            # 分别计算出当前位，高位，低位
            curr_bit = (n % (operator * 10)) // operator
            high_bit = n // (operator * 10)
            low_bit = n % operator
            print(curr_bit,high_bit,low_bit)

            # 根据当前位的大小，分为3中情况
            if curr_bit == 0:
                count += high_bit * operator
            if curr_bit == 1:
                count += high_bit * operator + low_bit + 1
            if curr_bit > 1:
                count += (high_bit + 1) * operator

            # 算子×10，起到移位的作用
            operator *= 10

        return count

"""
个位出现1的个数： 10132个
十位出现1的个数： 10135个
百位出现1的个数： 10200个
千位出现1的个数： 10315个
万位出现1的个数： 10000个
十万位出现1的个数： 1315个

"""
print(Solution().countDigitOne(101314))
