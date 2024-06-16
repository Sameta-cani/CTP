from itertools import combinations, product
from collections import Counter


def calculate_probabilities(dice: list) -> dict:
    num_dice = len(dice)
    possible_scores = Counter()
    
    for rolls in product(*dice):
        score = sum(rolls)
        possible_scores[score] += 1
    
    total_outcomes = 6 ** num_dice
    probabilities = {score: count / total_outcomes for score, count in possible_scores.items()}
    
    return probabilities

def solution(dice: list) -> list:
    n = len(dice) // 2
    max_win_prob = 0
    
    for A_indices in combinations(range(len(dice)), n):
        B_indices = [i for i in range(len(dice)) if i not in A_indices]
        
        A_dice = [dice[i] for i in A_indices]
        B_dice = [dice[i] for i in B_indices]
        
        A_probs = calculate_probabilities(A_dice)
        B_probs = calculate_probabilities(B_dice)
        
        win_prob = 0
        for a_score, a_prob in A_probs.items():
            for b_score, b_prob in B_probs.items():
                if a_score > b_score:
                    win_prob += a_prob * b_prob
        
        if win_prob > max_win_prob:
            max_win_prob = win_prob
            best_combination = A_indices
            
    ans = [val + 1 for val in best_combination]
    return ans