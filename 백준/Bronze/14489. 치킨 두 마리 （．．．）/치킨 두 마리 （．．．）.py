total = sum(map(int, input().split()))

C = int(input())

print(total - 2 * C if total >= 2 * C else total)