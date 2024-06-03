from collections import deque

def solution(cacheSize: int, cities: list) -> int:
    hit, miss = 1, 5
    if cacheSize == 0:
        return len(cities) * miss
    
    queue = deque(maxlen=cacheSize)
    cache = set()
    ans = 0

    for city in cities:
        city = city.lower()
        if city in cache:
            queue.remove(city)
            ans += hit
        else:
            if len(queue) == cacheSize:
                removed_city = queue.popleft()
                cache.remove(removed_city)
            ans += miss
        queue.append(city)
        cache.add(city)

    return ans
