from bisect import bisect_left, bisect_right
import sys
input = sys.stdin.readline

N = int(input())
N_cards = sorted(list(map(int, input().split())))
M = int(input())
M_cards = list(map(int, input().split()))

for card in M_cards:
    print(bisect_right(N_cards, card) - bisect_left(N_cards, card), end=' ')