class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paranthesis = {')':'(','}':'{',']':'['}
        for char in s:
            if char in paranthesis:
                top = stack.pop() if stack else '#'
                if paranthesis[char] != top:
                    return False
            else:
                stack.append(char)
        return not stack
if __name__=="__main__":
    s = "([)]"
    s1 = "(){}[]"
    s2 = "({[]})"
    print("Answer:", Solution().isValid(s))
    print("Answer:", Solution().isValid(s1))
    print("Answer:", Solution().isValid(s2))