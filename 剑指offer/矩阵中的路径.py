"""

请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一个格子开始，每一步可以在矩阵中向左，向右，向上，向下移动一个格子。
如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
例如 a b c e
    s f c s
    a d e e
这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，
但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入该格子。
"""

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        for i in range(rows):
            for j in range(cols):
                if matrix[i * cols + j] == path[0]:
                    if self.find_path(list(matrix), rows, cols, path[1:], i, j):
                        return True

    def find_path(self, matrix, rows, cols, path, i, j):
        if not path:
            return True
        matrix[i * cols + j] = 0
        if j + 1 < cols and matrix[i * cols + j + 1] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i, j + 1)
        elif j - 1 >= 0 and matrix[i * cols + j - 1] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i, j - 1)
        elif i + 1 < rows and matrix[(i + 1) * cols + j] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i + 1, j)
        elif i - 1 >= 0 and matrix[(i - 1) * cols + j] == path[0]:
            return self.find_path(matrix, rows, cols, path[1:], i - 1, j)
        else:
            return False


print(Solution().hasPath(["a", 'b', 'c', 'e', 's', 'f', 'c', 's', 'a', 'd', 'e', 'e'],3,4,'bcced'))
jdk-12.0.2


