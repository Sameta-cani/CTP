h, m = map(int, input().split())

new_h = (h - (m < 45)) % 24
new_m = (m - 45) % 60

print(new_h, new_m)