start_h, start_m = map(int, input().strip().split(':'))
end_h, end_m = map(int, input().strip().split(':'))

if end_m < start_m:
    end_m += 60
    start_h += 1
    
cnt = (end_m - start_m) + (end_h - start_h) % 24

print(cnt)
