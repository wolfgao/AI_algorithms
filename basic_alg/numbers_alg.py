
import math

class Solution:
    def reverse(self, x:int) -> int:
        '''
        https://leetcode.com/problems/reverse-integer/
        Change the integer to a string, then it is easy to exchange or switch the charactors or digits
        @:param 32bit int
        @:return 32bit int
        '''
        if x == 0:
            return 0
        # change to string
        s = "%d" % x

        # remove the tail 0
        s = s.strip('0')
        n = len(s)
        newX = ''
        if s[0] is '-':
            newX = '-'
            for i in range(n - 1, 0, -1):
                newX += s[i]
        else:
            for i in range(n - 1, -1, -1):
                newX += s[i]
        int_x = int(newX)

        # because it need return 32 bit int, the max number is 2^31
        if abs(int_x) > math.pow(2, 31):
            return 0
        else:
            return int_x

if __name__ == "__main__" :
    a=123
    b=-123
    c=-123000
    d=0
    e=1534236469
    f=-2147483648

    s=Solution()
    assert s.reverse(a) ==321
    assert s.reverse(b) == -321
    assert s.reverse(c) == -321
    assert s.reverse(d) == 0
    assert s.reverse(e) == 0
    assert s.reverse(f) == 0
