import functools
from collections import OrderedDict
import requests

def cache(max_limit=64):
    def internal(f):
        @functools.wraps(f)
        def deco(*args, **kwargs):
            cache_key = (args, tuple(kwargs.items()))
            if cache_key in deco._cache:
                deco._cache[cache_key][1] += 1
                deco._cache.move_to_end(cache_key, last=True)
                return deco._cache[cache_key]
            result = f(*args, **kwargs)
            if len(deco._cache) >= max_limit:
                min_use_key = min(deco._cache, key=lambda x: deco._cache[x][1])
                deco._cache.pop(min_use_key)
            deco._cache[cache_key] = [result, 1]
            return result
        deco._cache = OrderedDict()
        return deco
    return internal

@cache(max_limit=100)
def fetch_url(url, first_n=100):
    """Fetch a given url"""
    res = requests.get(url)
    return res.content[:first_n] if first_n else res.content


