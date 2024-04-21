def solution(n, arr1, arr2):
    answer = []
    for val1, val2 in zip(arr1, arr2):
        map1 = bin(val1)[2:].zfill(n)
        map2 = bin(val2)[2:].zfill(n)
        ans = ''
        for i, j in zip(map1, map2):
            ans += '#' if int(i) or int(j) else ' '
        answer.append(ans)
    return answer