from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for item in tokens:
            match item:
                case "+":
                    stack.append(stack.pop(-2) + stack.pop(-1))
                case "-":
                    stack.append(stack.pop(-2) - stack.pop(-1))
                case "/":
                    stack.append(int(stack.pop(-2) / stack.pop(-1)))
                case "*":
                    stack.append(stack.pop(-2) * stack.pop(-1))
                case _:
                    stack.append(int(item))
        return stack[0]
    

    ## Just for testing eval()
        # for item in tokens:
        #     if item.lstrip("-").isdigit():
        #         stack.append(item)
        #     else:
        #         stack.append(int(eval(f"{stack.pop(-2)} {item} {stack.pop(-1)}")))
        # return int(stack[0])

a = Solution()
print(a.evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
print(a.evalRPN(tokens = ["2","1","+","3","*"]))
print(a.evalRPN(tokens = ["4","13","5","/","+"]))