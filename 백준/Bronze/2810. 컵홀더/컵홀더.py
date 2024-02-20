# 좌석의 수 입력
N = int(input())

# 좌석의 정보 입력
seats = input()

# 커플석이 없다면 좌석 개수가 최대 사람의 수
# 커플석이 있다면 'LL'을 'L'으로 치환하고 +1
print(len(seats.replace('LL', 'L')) + 1 if seats.find('LL') != -1 else N)