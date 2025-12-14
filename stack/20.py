class Solution:
    def isValid(self, s: str) -> bool:
        # 剪枝：如果字符串长度是奇数，肯定无法完全匹配
        if len(s) % 2 == 1:
            return False
        
        # 建立映射表：右括号 -> 左括号
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        
        stack = []
        
        for char in s:
            if char in pairs:
                # 情况1：当前字符是右括号
                # 如果栈为空（没有左括号）或者 栈顶元素不匹配
                if not stack or stack[-1] != pairs[char]:
                    return False
                # 匹配成功，弹出栈顶的左括号
                stack.pop()
            else:
                # 情况2：当前字符是左括号
                stack.append(char)
        
        # 循环结束，栈必须为空才算有效
        return not stack