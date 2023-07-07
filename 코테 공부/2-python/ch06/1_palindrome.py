import collections
import re

class Palindrome:
    def is_palindrome(self,s:str) -> bool:
        strs =[]
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs)>1:
            if strs.pop(0) != strs.pop():
                return False
        return True

    def is_palindrome2(self,s:str) -> bool:
        strs=collections.deque()
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        while len(strs)>1:
            if strs.popleft() != strs.pop():
                return False
        return True

    def is_palindrome3(self,s:str)->bool:
        s=s.lower()
        s=re.sub('[^a-z0-9]','',s)
        return s==s[::-1]

palindrome=Palindrome()
k = "A man, a plan, a canal: Panama"
d = "race a car"

print(palindrome.is_palindrome(k))    # Expected: True
print(palindrome.is_palindrome2(k))   # Expected: True
print(palindrome.is_palindrome3(k))   # Expected: True
print(palindrome.is_palindrome(d))    # Expected: False
print(palindrome.is_palindrome2(d))   # Expected: False
print(palindrome.is_palindrome3(d))   # Expected: False
