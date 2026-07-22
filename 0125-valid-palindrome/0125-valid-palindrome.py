import re
class Solution(object):
    def isPalindrome(self, s):
        
        cleaned = re.sub(r"[^a-zA-Z0-9]","",s).lower()
        left=0
        right=len(cleaned)-1

        while left<right:
            if cleaned[left]==cleaned[right]:
                left+=1
                right-=1
            else :
                return False

        return True

        
        