while True:
    edges = list(map(int, input().split()))
    if edges == [0, 0, 0]:
        break
    max_edge = max(edges)
    sum_edge = sum(edges)
    unique_edges = len(set(edges))

    if sum_edge - max_edge <= max_edge:
        print('Invalid')
    elif unique_edges == 1:
        print('Equilateral')
    elif unique_edges == 2:
        print('Isosceles')
    else:
        print('Scalene')