for _ in range(int(input())):
    H, W, N = map(int, input().split())
    floor = N % H or H
    room = (N - 1) // H + 1
    print(f"{floor}{room:02d}")