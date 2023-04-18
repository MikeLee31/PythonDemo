class Solution:
    def isValid(self, s: str) -> bool:
        # 基础入栈出栈，408学过思路简单，用python队列模拟栈
        stack = []
        for i in s:
            if i == '(' or i == '[' or i == '{':
                stack.append(i)
                # print(stack)
            if len(stack)==0 and(i == ')' or i == ']' or i == '}'):
                return False
            if i == ')':
                # print(stack[-1])
                if '(' == stack[-1]:
                    stack.pop()
                else:
                    return False
            if i == ']':
                # print(stack[-1])
                if '[' == stack[-1]:
                    stack.pop()
                else:
                    return False
            if i == '}':
                # print(stack[-1])
                if '{' == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack)!= 0:
            return False
        return True

if __name__ == '__main__':
    print(Solution.isValid(123,"]"))