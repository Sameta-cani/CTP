import sys

input = sys.stdin.readline

total_seats = int(input())

seating_arrangement = input().rstrip()

max_people = (len(seating_arrangement.replace('LL', 'L')) + 1 
              if 'LL' in seating_arrangement else total_seats)
print(max_people)