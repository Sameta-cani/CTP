while True:
    edges = list(map(int, input().split()))
    unq_edges = set(edges)

    if unq_edges == {0}:
        break

    if max(edges) >= sum(edges) - max(edges):
        print("Invalid")
    else:
        if len(unq_edges) == 1:
            print("Equilateral")
        elif len(unq_edges) == 2:
            print("Isosceles")
        else:
            print("Scalene")