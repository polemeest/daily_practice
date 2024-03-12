class Solution:
    def calculate(self, s: str) -> int:
        def process_input(s: str) -> list:
            res = []
            negative = False
            for item in s.strip():
                if item == "-":
                    if res and res[-1] == "-":
                        negative = True
                if negative and not item.isdigit():
                    negative = False
                if negative:
                    res[-1] += item
                if item != " ":
                    res.append(item)
            return res
        

        def process_parenteses(s: str) -> str:
            stack = []
            for item in s:
                if item == ")" and stack:
                    expression = []
                    while True:
                        el = stack.pop()
                        if el == "(":
                            break
                        expression.append(el)
                    stack.append(parenteses_calculation(reversed(expression)))
                else:
                    stack.append(item)
            return stack


        def parenteses_calculation(s: list) -> int:
            stack = []
            operand = False
            for item in s:
                if item in ("+", "-"):
                    operand = item
                else:
                    stack.append(int(item))
                    if operand:
                        match operand:
                            case "+":
                                stack.append(stack.pop(-2) + stack.pop(-1))
                            case "-":
                                stack.append(stack.pop(-2) - stack.pop(-1))
                            case _:
                                pass
                        operand = False
            return stack[0]
        

        def resolve(s: list) -> int:
            temp = []
            negate = False
            for item in s:
                if not temp and item == "-":
                    negate = True
                elif item != "+" and item != "-":
                    if negate:
                        temp.append(-int(item))
                        negate = False
                    else:
                        temp.append(item)
                else:
                    temp.append(item)
            if len(temp) > 1:
                temp = parenteses_calculation(temp)
            else:
                temp = temp[0]
            return temp
        

        if "+" in s or "-" in s or "(" in s:
            s = process_input(s)
            if "(" in s:
                s = process_parenteses(s)
            s = resolve(s)
        

        return int(s)




a = Solution()
print(a.calculate(s = "(1+(4+5+2)-3)+(6+8)"))
print(a.calculate(s = "- (3 + (4 + 5))"))
print(a.calculate(s = "1 + 1"))
print(a.calculate(s = " 2-1 + 2 "))
print(a.calculate(s = "-2+ 1"))
