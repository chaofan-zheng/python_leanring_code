"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-anagram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isAnagram(self, s, t):
        dict_s = {}
        dict_t = {}
        if len(s) != len(t):
            return False
        for alpha in s:
            if alpha in dict_s:
                dict_s[alpha] += 1
            else:
                dict_s[alpha] = 1
        for alpha in t:
            if alpha in dict_t:
                dict_t[alpha] += 1
            else:
                dict_t[alpha] = 1
        for key, value in dict_s.items():
            if key in dict_t and dict_s[key] == dict_t[key]:
                continue
            else:
                return False
        return True
