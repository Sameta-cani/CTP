edges = sorted(list(map(int, input().split())))

if edges[0] + edges[1] > edges[2]:
    print(sum(edges))
else:
    print((edges[0] + edges[1]) * 2 - 1)