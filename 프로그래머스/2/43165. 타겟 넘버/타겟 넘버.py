def solution(numbers, target):
    memo = {}

    def DFS(idx, cur):
        if idx == len(numbers):
            return 1 if cur == target else 0
        
        if (idx, cur) in memo:
            return memo[(idx, cur)]
        
        positive = DFS(idx + 1, cur + numbers[idx])
        negative = DFS(idx + 1, cur - numbers[idx])

        memo[(idx, cur)] = positive + negative
        return memo[(idx, cur)]
    
    return DFS(0, 0)