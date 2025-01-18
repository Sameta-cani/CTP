N, A, B = map(int, input().split())

sub = N + B

if A > B:
    print("Subway")
elif A < B:
    print("Bus")
else:
    print("Anything")