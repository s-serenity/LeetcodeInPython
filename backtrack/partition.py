class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        res = []

        def if_palin(sub):
            return sub == sub[::-1]

        def dfs(s, idx, path):
            if idx == n:
                res.append(path.copy())
                return
            for i in range(idx, n):
                substring = s[idx:i+1]
                if if_palin(substring):
                    path.append(substring)
                    dfs(s, i + 1, path)
                    path.pop()

        dfs(s, 0, [])
        return res

s = "aab"
Solution.partition(s)