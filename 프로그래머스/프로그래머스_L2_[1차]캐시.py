"""
프로그래머스 [1차]캐시
난이도: LV2
유형: 스택
"""
def solution(cacheSize, cities):

    cache = []
    answer = 0
    # 대소문자 구분하지 않기 위해서 대문자로 바꿈
    cities = [c.upper() for c in cities]

    # 캐시에 아무것도 없다면 cache miss
    if cacheSize == 0:
        return len(cities) * 5
    else:
        for city in cities:
            # 데이터가 캐시에 없을 때
            if not city in cache:
                # 캐시가 허용된 용량보다 적게 들어있을 때 캐시에 데이터를 넣음
                if len(cache) < cacheSize:
                    cache.append(city)
                    answer += 5
                # 가장 처음에 넣었던 메모리를 빼고 데이터를 넣음
                else:
                    cache.pop(0)
                    cache.append(city)
                    answer += 5
            # 데이터에 캐시가 있을 때 cache hit
            else:
                cache.pop(cache.index(city))
                cache.append(city)
                answer += 1
    
    return answer
