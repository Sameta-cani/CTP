# 사용자로부터 3개의 데이터 조각 입력 받기
data = [tuple(input().split()) for _ in range(3)]

# 연도 데이터 추출 및 정렬
years = sorted([int(year) % 100 for _, year, _ in data])

# 이름 데이터 추출 및 정렬
names_sorted = sorted(data, key=lambda x: int(x[0]), reverse=True)
names = [name[0] for _, _, name in names_sorted]

# 결과 출력
print("".join(map(str, years)))
print("".join(names))