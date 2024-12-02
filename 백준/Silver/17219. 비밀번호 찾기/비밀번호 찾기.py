import sys
input = sys.stdin.readline

N, M = map(int, input().split())
log_info = {site: pw for site, pw in (input().strip().split() for _ in range(N))}

sys.stdout.write('\n'.join(log_info[input().strip()] for _ in range(M)) + '\n')