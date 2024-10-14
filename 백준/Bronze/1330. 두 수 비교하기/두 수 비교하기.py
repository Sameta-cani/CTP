import sys
input = sys.stdin.readline

A, B = map(int, input().split())

print(">" if A > B else ("==" if A == B else "<"))