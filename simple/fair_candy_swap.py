"""
888. 公平的糖果棒交换
"""


class Solution(object):
    def fairCandySwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        a = 0
        for i in A:
            a += i
        b = 0
        for i in B:
            b += i
        d_value = a - b
        half = d_value / 2
        for i in A:
            ib = i - half
            if ib in B:
                return [i, ib]


class SolutionPro(object):
    def fairCandySwap(self, A, B):
        a = 0
        for i in A:
            a += i
        b = 0
        for i in B:
            b += i
        d_value = a - b
        half = d_value / 2
        A = sorted(A)
        B = sorted(B)
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] - half == B[j]:
                return [A[i], B[j]]
            elif A[i] - half > B[j]:
                j += 1
            else:
                i += 1


class SolutionPlusPro(object):
    def fairCandySwap(self, A, B):
        a = sum(A)
        b = sum(B)
        d_value = a - b
        half = d_value / 2
        A = sorted(A)
        B = sorted(B)
        i = 0
        j = 0
        while i < len(A) and j < len(B):
            if A[i] - half == B[j]:
                return [A[i], B[j]]
            elif A[i] - half > B[j]:
                j += 1
            else:
                i += 1


if __name__ == "__main__":
    A = [1, 1]
    B = [2, 2]
    solution = SolutionPlusPro()
    print(solution.fairCandySwap(A, B))
