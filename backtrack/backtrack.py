from typing import List

def get_sum(a):
    res = 0
    for x in a:
        res += x
    return res


class Solution:
    def __init__(self):
        self.res = []
        self.track = []

    def backtrack(self, k, n, used,start):
        if len(self.track) == k and get_sum(self.track) == n:
            self.res.append(list(self.track))
            return

        if get_sum(self.track) > n:
            return

        for i in range(start, 10):
            if used[i]:
                continue
            self.track.append(i)
            used[i] = True
            self.backtrack(k, n, used,i+1)
            self.track.pop()
            used[i] = False

    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        used = [False] * 10
        self.backtrack(k, n, used,1)
        return self.res

s = Solution()
k = 3
n = 7
print(s.combinationSum3(k,n))