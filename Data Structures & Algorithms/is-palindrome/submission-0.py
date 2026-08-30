class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_str = ''
        for i in s:
            if i.isalnum():
                new_str += i.lower()
        L = 0
        R = len(new_str) - 1
        while L <= R:
            if new_str[L] != new_str[R]:
                return False
            L += 1
            R -= 1
        return True
        


        
        