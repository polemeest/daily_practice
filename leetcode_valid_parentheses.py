class Solution:
    def isValid(self, s: str) -> bool:
        keys = {")": "(", "]": "[", "}": "{"}
        new = ""
        for i, v in enumerate(s):
            if v in ")]}":
                if new and new[-1] == keys[v]:
                   new = new[:-1]
                else:
                    return False 
            else:
                new += v
        return not new

        # keys = {")": "(", "]": "[", "}": "{"}
        # stack = []
        # for v in s:
        #     if v in "([{":
        #         stack.append(v)
        #     else:
        #         if not stack or stack.pop() != keys[v]:
        #             return False
        # return not stack
    

        # keys = {")": "(", "]": "[", "}": "{"}
        # stack = ""
        # for v in s:
        #     if v in "([{":
        #         stack += v
        #     else:
        #         if not stack or stack[-1] != keys[v]:
        #             return False
        #         else:
        #             stack = stack[:-1]
        # return not stack



a = Solution()
# print(a.isValid(s = "()"))
print(a.isValid(s = "()[]{}"))
print(a.isValid(s = "(]"))
print(a.isValid(s = "([)]"))
print(a.isValid(s = "){"))