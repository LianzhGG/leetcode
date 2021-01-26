"""
给你一个由一些多米诺骨牌组成的列表 dominoes。

如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。

形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。

在 0 <= i < j < dominoes.length 的前提下，找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        if len(dominoes) == 1:
            return 0
        # for i in range(len(dominoes)):
        total = 0
        # for domino1 in dominoes:
        domino1 = dominoes[0]
        remove: List[List[int]] = []
        # 找到1个，count=1 找到两个，count=2+1 找到3个 count=3+2+1
        # 将找到的全部放进remove中，遍历完一遍以后，从dominoes中将remove移除，然后再接着遍历
        count = 0
        remove.append(domino1)
        for domino2 in dominoes[1:]:
            if (domino1[0] == domino2[0] and domino1[1] == domino2[1]) or (
                    domino1[0] == domino2[1] and domino1[1] == domino2[0]):
                count += 1
                remove.append(domino2)
        # dominoes = [dominoes[j] for j in range(len(remove)) if (dominoes[j] not in remove)]
        dominoes = list(filter(lambda ds: ds not in remove, dominoes))
        total += self._factorial(count)
        total += self.numEquivDominoPairs(dominoes)
        return total

    def _factorial(self, a: int):
        result = 1
        for i in range(2, a + 1):
            result *= i
        return result


if __name__ == "__main__":
    d = [[1, 2], [2, 1], [1, 2], [1, 2], [3, 4], [3, 4], [5, 6]]
    s = Solution()
    result = s.numEquivDominoPairs(d)
    print(result)
