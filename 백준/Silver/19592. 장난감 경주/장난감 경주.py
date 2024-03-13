T = int(input())

for _ in range(T):
    N, X, Y = map(int, input().split())
    Vs = list(map(int, input().split()))

    # 단독 우승에 필요한 기준 시간 계산
    base_time = X / max(Vs)

    # 내 속도
    my_V = Vs[-1]

    # 부스터를 안 써도 되는 경우: 이미 가장 빠르면 부스터 필요 없음
    if max(Vs[:-1]) < my_V:
        print(0)
    else:
        start, end = 0, Y
        result = -1
        # 부스터를 써야 하는 경우 이분 탐색
        while start <= end:
            # 부스터를 써서 갈 거리
            mid = (start + end) // 2
            # 해당 거리를 갔을 때의 내 시간
            my_time = 1 + (X - mid) / Vs[N - 1]
            # 내 시간이 기준 시간보다 빠를 경우
            if my_time < base_time:
                result = mid # 부스터 사용으로 단독 우승 가능
                end = mid - 1 # 더 적은 부스터 사용 거리를 찾기
            # 내 시간이 기준 시간보다 느릴 경우
            # 부스터로 가는 거리를 늘림
            else:
                start = mid + 1 

        print(result if result <= Y else -1) # 결과가 Y 이하인 경우에만 유효
