def is_every_point_lit(lamps, height):
    last_lit = 0  # 이전 가로등이 비춘 마지막 지점
    for lamp in lamps:
        if lamp - height <= last_lit:  # 현재 가로등이 이전 가로등의 범위를 커버하면
            last_lit = lamp + height  # 마지막으로 비춘 지점 갱신
        else:
            return False  # 커버하지 못하는 경우가 있으면 False 반환
    return last_lit >= N  # 마지막 가로등이 굴다리 끝까지 비추는지 확인

N = int(input())
M = int(input())
lamps = sorted(map(int, input().split()))  # 가로등 위치 정렬

start, end = 1, N  # 가능한 높이의 범위
result = N  # 가능한 최소 높이

while start <= end:
    mid = (start + end) // 2
    if is_every_point_lit(lamps, mid):
        result = min(result, mid)  # 최소 높이 갱신
        end = mid - 1  # 더 낮은 높이 탐색
    else:
        start = mid + 1  # 높은 높이에서 탐색

print(result)