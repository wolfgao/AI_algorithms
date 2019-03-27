from typing import List


class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        Try to get the largest prefex string which are same or common in this list.
        :param strs:
        :return: str: the largest prefix string are common in the list
        '''
        # check if the strs is empty
        if len(strs) == 0:
            return ''

        # strs is not empty
        prefix = ""  # type: str

        # get the length of the minimum string
        min_len = len(strs[0])
        for str in strs:
            if len(str) < min_len:
                min_len = len(str)

        # go through the string list to get the common prefix
        i = 0
        for i in range(min_len):
            p = strs[0][i]
            prefix += p
            for str in strs:
                if p != str[i]:
                    prefix = prefix[:i]
                    print(prefix, i)
                    return prefix
        return prefix

    def isValid(self, s: str) -> bool:
        '''
        This method is to check if the input has valid brackets.
        :param s:
        :return: bool
        '''
        if len(s) <=0: return None
        bra_strs = {'(': ')', '{': '}', '[': ']'}
        cc_strs = []
        i=0
        while i<len(s):

            if len(cc_strs) > 0:
                if bra_strs.get(cc_strs[-1]) == s[i]:
                    end=len(cc_strs)
                    cc_strs = cc_strs[:end-1]
                    i += 1
                    continue
            if i<len(s):
                cc_strs.append(s[i])
            i += 1

        #if cc_strs has something, return false
        if cc_strs:
            print(cc_strs)
            return False
        else:
            return True

    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        https://leetcode.com/problems/longest-substring-without-repeating-characters/
        Given a string, find the length of the longest substring without repeating characters.
        O(n^3) way:
        1) get all substrings, 2) check if all substrings contain unique charactors, then get the max
        O(2n) way:
        sliding window with unique charactors, when sliding window moves, to check which is the max?
        :param s:
        :return: int the length of the longest substring
        '''
        s_len = len(s)
        if s_len <= 0: return 0

        # moving windows to find all unique substrings
        sliding_windows = []
        common = ''
        for i in range(s_len):
            if s[i] not in common: # 如果不重复，就加入
                common +=s[i]
                #到最后一个元素了
                if i == s_len -1: # 如果是最后一个字符，就尽快加入到后面代检查的数组中
                    sliding_windows.append(common)
            else: # 如果重复就后移，找到相重复的字符位置，位移
                sliding_windows.append(common)
                start_index = common.index(s[i])
                common = common[start_index+1:] + s[i]
        max=0
        #打印所以找到的uniqe substring
        print(sliding_windows)
        index = max_index = 0
        for substring in sliding_windows:
            if max < len(substring):
                max = len(substring)
                max_index = index
            index += 1
        print(sliding_windows[max_index])
        return max

if __name__ == '__main__':
    '''
    s1="()"
    s2="()[]{}"
    s3="(]"
    s4="([)]"
    s5="{[]}"
    print(Solution().isValid(s1))
    print(Solution().isValid(s2))
    print(Solution().isValid(s3))
    print(Solution().isValid(s4))
    print(Solution().isValid(s5))
    '''
    s6 = "abcabcbb"
    s7 = "bbbbb"
    s8 = "pwwkew"
    s9 = "anviaj"
    s10 = "ohvhjdml"
    print(Solution().lengthOfLongestSubstring(s6))
    print(Solution().lengthOfLongestSubstring(s7))
    print(Solution().lengthOfLongestSubstring(s8))
    print(Solution().lengthOfLongestSubstring(s9))
    print(Solution().lengthOfLongestSubstring(s10))