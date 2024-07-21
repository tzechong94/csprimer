import urllib.request
from collections import OrderedDict


def memoize(fn, maxsize=128):
    cache = OrderedDict()

    def inner(arg):
        if arg in cache:
            cache.move_to_end(arg)
            return cache[arg]
        res = fn(arg)
        cache[arg] = res

        if len(cache) > maxsize:
            cache.popitem(last=False)
        return res
        # do the caching logic
        # falling back to function if needed

    return inner


def fetch(url, blah="blah"):

    with urllib.request.urlopen(url) as response:
        content = response.read().decode("utf-8")
        return content


@memoize  # decorator, wrap below function with memorize logic
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == "__main__":
    # fetch = memoize(fetch, key_func=lambda url, blah: url)
    # print(fetch("http://google.com")[:80])
    # print(fetch("http://google.com")[80:160])
    # print(fetch("http://google.com")[160:240])
    # print(fetch("http://google.com")[240:320])

    # #
    # fib = memoize(fib)  # use fib instead of cache_fib because in the
    # recursion fib is called multiple times
    print(fib(35))
