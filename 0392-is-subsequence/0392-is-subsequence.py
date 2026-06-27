class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
    
        S = len(s)
        T = len(t)
        if s == '': return True
        if S > T: return False
 
        j = 0
        for i in range(T):
            if t[i] == s[j]:
                if j == S-1:
                    return True
                j += 1
        
        return False