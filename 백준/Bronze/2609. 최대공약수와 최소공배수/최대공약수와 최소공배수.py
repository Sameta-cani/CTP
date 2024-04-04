def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
    
n1, n2 = map(int, input().split())
g = gcd(n1, n2)

print(g, n1 * n2 // g, sep='\n')