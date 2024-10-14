from timeit import timeit
import functools

@functools.lru_cache(maxsize=None)
def kol_les_mem(n, k):
    if n == 0:
        return 1
    ans = 0

    for i in range(k + 1, n + 1):
        ans += kol_les_mem(n - i,  i)
    return ans


setup_code_mem = 'from __main__ import kol_les_mem'
stmt_mem = 'kol_les_mem(25, 0)'
print(
    'Время выполнения с мемоизацией: ',
    timeit(
        setup=setup_code_mem,
        stmt=stmt_mem,
        number=20000
    )
)