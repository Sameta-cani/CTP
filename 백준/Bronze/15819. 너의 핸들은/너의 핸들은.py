N, I = map(int, input().split())
handles = sorted([input() for _ in range(N)])

print(handles[I-1])