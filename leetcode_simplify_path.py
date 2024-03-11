class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        for el in path.strip("/").split("/"):
            if el == "..":
                if stack:
                    stack.pop()
            elif el not in ('.', '/', ''):
                stack.append(el)

        
        print("/" + "/".join(stack))



a = Solution()
a.simplifyPath(path = "/home//foo/")
a.simplifyPath(path = "/home/")
a.simplifyPath(path = "/../")
a.simplifyPath(path = "/home/./foo/")
a.simplifyPath(path = "/a/./b/../../c/")