from functools import lru_cache


mod = 10**9 + 7


@lru_cache(maxsize=1000)
def solve(n):
    if n == 0:
        return 1
    ans = 0
    for i in range(1, 7):
        if n - i >= 0:
            ans = (ans + solve(n - i)) % mod

    return ans


n = int(input())
print(solve(n))
