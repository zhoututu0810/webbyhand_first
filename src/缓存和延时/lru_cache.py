from functools import lru_cache

# @functools.lru_cache(maxsize=None, typed=False)
#
# 使用functools模块的lur_cache装饰器，可以缓存最多 maxsize 个此函数的调用结果，从而提高程序执行的效率，特别适合于耗时的函数。
# 参数maxsize为最多缓存的次数，如果为None，则无限制，设置为2n时，性能最佳；如果 typed=True（注意，在 functools32 中没有此参数），
# 则不同参数类型的调用将分别缓存，例如 f(3) 和 f(3.0)。
#
# 被 lru_cache 装饰的函数会有 cache_clear 和 cache_info 两个方法，分别用于清除缓存和查看缓存信息。


@lru_cache(None)
def add(x, y):
    print("calculating: %s + %s" % (x, y))
    return x + y


print(add(1, 2))
print(add(1, 2))
print(add(2, 3))
print()
print(add.cache_info())     # CacheInfo(hits=1, misses=2, maxsize=None, currsize=2)
print(dir(add.cache_info()))
print('清除缓存')
print(add.cache_clear())
print(add.cache_info())     # CacheInfo(hits=0, misses=0, maxsize=None, currsize=0)

# 输出结果：
#
# calculating: 1 + 2
# 3
# 3
# calculating: 2 + 3
# 5
# 从结果可以看出，当第二次调用 add(1, 2) 时，并没有真正执行函数体，而是直接返回缓存的结果。
