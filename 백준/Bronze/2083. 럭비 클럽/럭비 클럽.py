while True:
    name, age, weight = input().split()
    if name == '#':
        break
    
    res = ''
    age, weight = int(age), int(weight)
    if age > 17 or weight >= 80:
        res = 'Senior'
    else:
        res = 'Junior'
        
    print(f"{name} {res}")