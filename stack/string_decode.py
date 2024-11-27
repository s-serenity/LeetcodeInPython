class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = ""
        for x in s:
            if x!="]":
                stack.append(x)
            else:
                num = ""
                z = ""
                while stack:
                    y = stack.pop()
                    if y=="[":
                        break
                    z += y
                print_z = z[::-1]
                while stack:
                    num+=stack.pop()
                num = int(num[::-1])
                res += print_z*num
        return res

s = "3[a]2[bc]"
Solution().decodeString(s)