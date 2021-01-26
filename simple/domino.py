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
        if len(dominoes) <= 1:
            return 0
        total = 0
        domino1 = dominoes[0]
        remove: List[List[int]] = []
        count = 0
        remove.append(domino1)
        for domino2 in dominoes[1:]:
            if (domino1[0] == domino2[0] and domino1[1] == domino2[1]) or (
                    domino1[0] == domino2[1] and domino1[1] == domino2[0]):
                count += 1
                remove.append(domino2)
        dominoes = list(filter(lambda ds: ds not in remove, dominoes))
        total += self._factorial(count)
        total += self.numEquivDominoPairs(dominoes)
        return total

    def _factorial(self, a: int):
        if a == 0:
            return 0
        result = 1
        for i in range(2, a + 1):
            result += i
        return result


if __name__ == "__main__":
    d = [[1, 1], [2, 2], [1, 1], [1, 2], [1, 2], [1, 1]]
    s = Solution()
    result = s.numEquivDominoPairs(d)
    print(result)
"""
这也太强了吧
public int numEquivDominoPairs(int[][] dominoes) {
        int ans = 0;
        int[] cp = new int[100];
        for(int[] arr:dominoes){
            Arrays.sort(arr);
            ans+=cp[arr[0]*10+arr[1]]++;
        }
        return ans;
}
"""

"""
class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        int[] map = new int[100];
        int res = 0;
        for(int i = 0; i < dominoes.length; i++){
            int m = dominoes[i][0];
            int n = dominoes[i][1];
            int k = m > n ? m * 10 + n : n * 10 + m;
            map[k] ++;
        }
        for(int i = 0; i < 100; i++){
            res += map[i] * (map[i] - 1) / 2;
        }
        return res;
    }
}
"""
"""
这道题还是挺巧妙的，因为两个数字都小于9，所以可以拼接成一个数字。不过解决这类计数问题比较通用的还是哈希表。
"""
"""
Java 哈希表 + 排列组合：

1、每个dominoes进行排序，按照key = ints[0] + "," + ints[1]与出现次数构建哈希表；

2、每种次数两两组合，累加就是答案。
   public int numEquivDominoPairs(int[][] dominoes) {
        if (dominoes.length == 0) {
            return 0;
        }
        Map<String, Integer> map = new HashMap<>();
        int res = 0;

        for (int[] ints : dominoes) {
            Arrays.sort(ints);
            String key = ints[0] + "," + ints[1];
            map.put(key, map.getOrDefault(key, 0) + 1);
        }
        for(int value :map.values()) {
            if (value == 1) {
                continue;
            }
            int num = value * (value - 1) / 2;
            res = res + num;
        }
        return res;
    }
"""

"""
方法一：二元组表示 + 计数
思路及解法

本题中我们需要统计所有等价的多米诺骨牌，其中多米诺骨牌使用二元对代表，「等价」的定义是，在允许翻转两个二元对的的情况下，使它们的元素一一对应相等。

于是我们不妨直接让每一个二元对都变为指定的格式，即第一维必须不大于第二维。这样两个二元对「等价」当且仅当两个二元对完全相同。

注意到二元对中的元素均不大于 99，因此我们可以将每一个二元对拼接成一个两位的正整数，即 (x, y) \to 10x + y(x,y)→10x+y。这样就无需使用哈希表统计元素数量，而直接使用长度为 100100 的数组即可。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/solution/deng-jie-duo-mi-nuo-gu-pai-dui-de-shu-li-yjlz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        num = [0] * 100
        ret = 0
        for x, y in dominoes:
            val = (x * 10 + y if x <= y else y * 10 + x)
            ret += num[val]
            num[val] += 1
        return ret

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/solution/deng-jie-duo-mi-nuo-gu-pai-dui-de-shu-li-yjlz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

复杂度分析

时间复杂度：O(n)O(n)，其中 nn 是多米诺骨牌的数量。我们至多只需要遍历一次该数组。

空间复杂度：O(1)O(1)，我们只需要常数的空间存储若干变量。

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/solution/deng-jie-duo-mi-nuo-gu-pai-dui-de-shu-li-yjlz/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""

"""
📖 文字解析
多米诺骨牌「等价」的概念：两张多米诺骨牌，对应相等或者 交叉 对应相等。可以声明一个计数器 count，枚举所有骨牌对，如果骨牌对等价，给计数器 count 加 11。时间复杂度为 O(N^2)O(N 
2
 )，这里 NN 是输入数组的长度。注意到题目给出的提示：1 <= dominoes.length <= 40000，O(N^2)O(N 
2
 ) 的解法不能通过测评。因此须要在遍历的时候记住一些信息。

方法一：哈希表
把有序数对封装成类，每一个多米诺骨牌就对应了类的一个对象；
在遍历的过程中使用哈希表记录出现的数对的数量。注意：有序数对中只要出现的字符对应相等或者交叉对应相等，在哈希表中就认为它们相等，因此须要 重写 hashCode() 方法、 equlas() 方法。例如 [1, 2] 和 [2, 1] 就须要认为是等价的对象；
假设某一类「等价」的对象的总数为 NN，这一类中任意取出 22 个的组合数 C_N^2 = \frac{N(N - 1)}{2}C 
N
2
​	
 = 
2
N(N−1)
​	
  就是这一类对总的「满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量」。对每一类的频数依次求频数对 22 的组合数，再求和即可（其实也可以一遍遍历，一遍用加法计算，我们放在方法二里介绍）。
参考代码 1：

作者：LeetCode
链接：https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/solution/deng-jie-duo-mi-nuo-gu-pai-dui-de-shu-li-08z8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

import java.util.HashMap;
import java.util.Map;

public class Solution {

    public int numEquivDominoPairs(int[][] dominoes) {
        // 为了避免哈希表自动扩容，根据题目的数据范围，设置哈希表初始化的大小为 100
        // Pair 类重写了 hashCode() 和 equals() 方法
        Map<Pair, Integer> freq = new HashMap<>(100);
        for (int[] dominoe : dominoes) {
            Pair key = new Pair(dominoe[0], dominoe[1]);
            freq.put(key, freq.getOrDefault(key, 0) + 1);
        }

        // 根据组合数公式 C_n^2 = (n * (n - 1)) / 2 计算等价骨牌能够组成的组合数，再求和
        int count = 0;
        for (int f : freq.values()) {
            count += (f * (f - 1)) / 2;
        }
        return count;
    }

    private class Pair {

        private int key;
        private int value;

        public Pair(int key, int value) {
            this.key = key;
            this.value = value;
        }

        /**
         * 让有序数对 [a, b] 和 [b, a] 认为是相等的对象
         *
         * @param o
         * @return
         */
        @Override
        public boolean equals(Object o) {
            if (this == o) {
                return true;
            }
            if (o == null || getClass() != o.getClass()) {
                return false;
            }
            Pair pair = (Pair) o;
            return key == pair.key && value == pair.value || key == pair.value && value == pair.key;
        }

        /**
         * 让相同的数对映射到同一个位置
         *
         * @return
         */
        @Override
        public int hashCode() {
            if (key > value) {
                return value * 10 + key;
            }
            return key * 10 + value;
        }
    }
}

作者：LeetCode
链接：https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/solution/deng-jie-duo-mi-nuo-gu-pai-dui-de-shu-li-08z8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

复杂度分析

时间复杂度：O(N)O(N)，其中 NN 是输入数组的长度；
空间复杂度：O(A)O(A)，这里 AA 是哈希表中键的总数。
"""

"""
把有序数对封装成一个类是相对麻烦的，根据题目给出的提示 1 <= dominoes[i][j] <= 9，我们可以 把有序数对拼成一个二位数。

方法二：根据题目给出的数据范围把有序整数拼成一个二位数
为了使得「等价」更易于比较，我们都让较小的数排在前面。例如：让 [1, 4] 拼成 14，让 [4, 1] 也拼成 14。

这样一来，在遍历的时候，「比较两个有序数组是否对应相等或者交叉相等」就等价于「比较两个整数的值」是否相等，以简化编码。

哈希表的键和值都是整数，并且键表示的两位整数的最大值是 9999，我们可以用数组代替哈希表，数组的下标就对应了原来使用的哈希表的键。

在遍历的时候用加法：每遍历到一个在哈希表（数组）中已经存在的骨牌，就给计数器加上此时这个骨牌在哈希表中已经记录的数量，因为当前这个骨牌和已经存在的骨牌中的每一个都等价，然后在给对应的哈希表（数组）中已经存在的骨牌数 +1+1。

参考代码 2：

作者：LeetCode
链接：https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/solution/deng-jie-duo-mi-nuo-gu-pai-dui-de-shu-li-08z8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
public class Solution {

    public int numEquivDominoPairs(int[][] dominoes) {
        int[] freq = new int[100];

        int count = 0;
        for (int[] dominoe : dominoes) {
            if (dominoe[0] > dominoe[1]) {
                int temp = dominoe[0];
                dominoe[0] = dominoe[1];
                dominoe[1] = temp;
            }

            int num = dominoe[0] * 10 + dominoe[1];
            count += freq[num];
            freq[num]++;
        }
        return count;
    }
}

作者：LeetCode
链接：https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/solution/deng-jie-duo-mi-nuo-gu-pai-dui-de-shu-li-08z8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

复杂度分析

时间复杂度：O(N)O(N)，这里 NN 是输入数组的长度；
空间复杂度：O(A^2)O(A 
2
 )，这里 AA 表示为骨牌数值的最大值，\log_{10} Alog 
10
​	
 A 表示 AA 的位数。根据时间复杂度的记法，O(\log_{10}A) = O(\log_{2}A) = O(\log A)O(log 
10
​	
 A)=O(log 
2
​	
 A)=O(logA)。需要的空间为 10^{\log_{10}A} \times A + A10 
log 
10
​	
 A
 ×A+A，再根据对指数恒等式，10^{\log_{10}A} \times A + A = A^2 + A10 
log 
10
​	
 A
 ×A+A=A 
2
 +A，因此空间复杂度为 O(A^2)O(A 
2
 )（视频有误，以文字题解为准）。

作者：LeetCode
链接：https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/solution/deng-jie-duo-mi-nuo-gu-pai-dui-de-shu-li-08z8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

把两个有序整数用一个整数表示，其实是比较常见的「状态压缩」。感兴趣的朋友可以尝试解决以下问题理解「状态压缩」技巧的应用。

练习
「力扣」第 1371 题：每个元音包含偶数次的最长子字符串（中等）；
「力扣」第 1457 题：二叉树中的伪回文路径（中等）。

作者：LeetCode
链接：https://leetcode-cn.com/problems/number-of-equivalent-domino-pairs/solution/deng-jie-duo-mi-nuo-gu-pai-dui-de-shu-li-08z8/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""