class Reverse:
    def reverseString(self, s:list[str])->None:
        left,right=0, len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1

    def reverseString2(self, s:list[str]) -> None:
        s.reverse()

    def reverseString3(self, s:list[str]) -> None:
        s[:]=s[::-1]

input=["h","e","l","l","o"]
input2=["H","a","n","n","a","h"]

reverse=Reverse()

reverse.reverseString(input)    
print(input)   # Outputs: ['o', 'l', 'l', 'e', 'h']
reverse.reverseString2(input)
print(input)   # Outputs: ['h', 'e', 'l', 'l', 'o']
reverse.reverseString3(input)
print(input)   # Outputs: ['o', 'l', 'l', 'e', 'h']

reverse.reverseString(input2)
print(input2)  # Outputs: ['h', 'a', 'n', 'n', 'a', 'H']
reverse.reverseString2(input2)
print(input2)  # Outputs: ['H', 'a', 'n', 'n', 'a', 'h']
reverse.reverseString3(input2)
print(input2)  # Outputs: ['h', 'a', 'n', 'n', 'a', 'H']
