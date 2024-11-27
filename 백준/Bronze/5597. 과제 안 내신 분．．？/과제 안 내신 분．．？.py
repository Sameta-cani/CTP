att = [1] * 31
for _ in range(28):
    att[int(input())] = 0

for idx in range(1, len(att)):
    if att[idx]:
        print(idx)