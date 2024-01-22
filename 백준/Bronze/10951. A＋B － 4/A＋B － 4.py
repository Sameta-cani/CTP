import sys

# 무한 루프를 돌며
while True:
  # try 구문을 실행하며
  try:
    # A와 B 입력
    A, B = map(int, sys.stdin.readline().split())
    # 합 출력
    print(A + B)
  # try 구문이 에러(ValeuError)가 나면
  except:
    # 무한루프를 멈추고 종료
    break