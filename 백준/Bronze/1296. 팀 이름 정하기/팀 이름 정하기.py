import sys

name = sys.stdin.readline().rstrip()
N = int(sys.stdin.readline().rstrip())
probs = []

for _ in range(N):
    team_name = sys.stdin.readline().rstrip()
    nums = []
    for ch in ['L', 'O', 'V', 'E']:
        nums.append(name.count(ch) + team_name.count(ch))
    prob = (nums[0] + nums[1]) * (nums[0] + nums[2]) * (nums[0] + nums[3])\
            * (nums[1] + nums[2]) * (nums[1] + nums[3]) * (nums[2] + nums[3])
    probs.append((team_name, prob % 100))

probs.sort(key=lambda x: x[0])
probs.sort(key=lambda x: x[1], reverse=True)

sys.stdout.write(probs[0][0])