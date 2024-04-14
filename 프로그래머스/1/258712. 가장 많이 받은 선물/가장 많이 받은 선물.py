def solution(friends, gifts):
    from collections import defaultdict
    
    answer = 0
    A_to_B = defaultdict(list)
    B_to_A = defaultdict(list)
    gift_score = dict()
    res = dict()
    
    for data in gifts:
        A, B = data.split()
        A_to_B[A].append(B)
        B_to_A[B].append(A)
        
    for name in friends:
        gift_score[name] = len(A_to_B[name]) - len(B_to_A[name])
        

    for name in friends:
        res[name] = 0
        for other in friends:
            give = A_to_B[name].count(other)
            given = A_to_B[other].count(name)

            if give > given:
                res[name] += 1
            elif give == given:
                if gift_score[name] > gift_score[other]:
                    res[name] += 1
        
    answer = max(res.values())
    
    return answer