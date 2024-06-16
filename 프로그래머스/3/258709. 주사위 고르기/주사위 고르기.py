from itertools import combinations, product
from collections import Counter

def calculate_distribution(dice):
    """각 주사위 조합의 가능한 점수 분포를 계산합니다."""
    distributions = []
    for die in dice:
        distributions.append(Counter(die))
    return distributions

def calculate_probabilities(dice):
    """주사위 조합의 모든 가능한 점수와 그 확률을 계산합니다."""
    num_dice = len(dice)
    possible_scores = Counter()
    
    for rolls in product(*dice):
        score = sum(rolls)
        possible_scores[score] += 1
    
    total_outcomes = 6 ** num_dice
    probabilities = {score: count / total_outcomes for score, count in possible_scores.items()}
    
    return probabilities

def expected_value(probabilities):
    """확률 분포에 기반한 기대값을 계산합니다."""
    return sum(score * prob for score, prob in probabilities.items())

def win_probability(A_probs, B_probs):
    """A가 B를 이길 확률을 계산합니다."""
    win_prob = 0
    for a_score, a_prob in A_probs.items():
        for b_score, b_prob in B_probs.items():
            if a_score > b_score:
                win_prob += a_prob * b_prob
    return win_prob

def solution(dice):
    n = len(dice) // 2
    max_win_prob = 0
    best_combination = []

    for A_indices in combinations(range(len(dice)), n):
        B_indices = [i for i in range(len(dice)) if i not in A_indices]
        
        A_dice = [dice[i] for i in A_indices]
        B_dice = [dice[i] for i in B_indices]
        
        A_probs = calculate_probabilities(A_dice)
        B_probs = calculate_probabilities(B_dice)
        
        win_prob = win_probability(A_probs, B_probs)
        
        if win_prob > max_win_prob:
            max_win_prob = win_prob
            best_combination = A_indices

    ans = [val + 1 for val in best_combination]
    return ans