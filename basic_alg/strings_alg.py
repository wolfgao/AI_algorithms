from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # check if the strs is empty
        if len(strs) == 0:
            return ''

        # strs is not empty
        prefix = ""  # type: str
        min_len = len(strs[0])
        for str in strs:
            if len(str) < min_len:
                min_len = len(str)
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

if __name__ == '__main__':
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