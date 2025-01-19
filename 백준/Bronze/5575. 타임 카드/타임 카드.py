for _ in range(3):
    data = list(map(int, input().split()))
    ans = (data[3] - data[0]) * 3600 + (data[4] - data[1]) * 60 + data[5] - data[2]
    print(ans // 3600, (ans % 3600) // 60, ans % 60)