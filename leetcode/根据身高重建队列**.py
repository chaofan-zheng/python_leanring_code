"""

假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对(h, k)表示，其中h是这个人的身高，k是排在这个人前面且身高大于或等于h的人数。 编写一个算法来重建这个队列。

注意：
总人数少于1100人。

示例

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""


class Solution:
    def reconstructQueue(self, people):
        people.sort(key=lambda x: (x[0], -x[1]))  # lambada 是一个隐函数，x表示列表中的一个元素，x只是临时起的一个名字，你可以使用任意的名字
        # x[0]表示列表里的第一个元素，默认是升序排列，reverse可以默认值为False。这句话的意思是一纬按照升序排列，二维按照降序。
        # 经过排序之后，我们会发现：身高高的人插在身高矮的人面前，必定会对矮的人的k造成影响。然而，身高矮的人插在身高高的人面前必定不会产生影响。
        # 因此 我们可以先做一个跟人数一样多的空的数列。第 i个人的位置，就是队列中从左往右数第k+1个「空」位置。

        # print(people)
        n = len(people)
        ans = [[] for _ in range(n)] # 创建空数列
        for person in people:
            spaces = person[1] + 1
            for i in range(n):
                if not ans[i]: # 如果不是False 等同于ans[i]为0的时候是True，space-1
                    spaces -= 1
                    if spaces == 0: # 如果space为0了 那就是找到了，这个空位就是person
                        ans[i] = person
                        break
        return ans


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
Solution().reconstructQueue(people)

# 作者：LeetCode-Solution
# 链接：https://leetcode-cn.com/problems/queue-reconstruction-by-height/solution/gen-ju-shen-gao-zhong-jian-dui-lie-by-leetcode-sol/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
