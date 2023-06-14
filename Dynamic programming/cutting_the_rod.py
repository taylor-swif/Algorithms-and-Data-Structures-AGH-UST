# We have long rods that we want to sell. 
# There is given array p, where pi is equal to the price of rod length i.
# Management of our company wants to know where the rods should be undercut in order to earn the most

def cut_rod_rek(p, n):
    if n == 1:
        return p[0]
    
    q = p[n - 1]
    for i in range(1, n):
        q = max(q, p[i - 1] + cut_rod_rek(p, n - i))
    return q

def cut_rod_mem(p, n):
    r = [0 for _ in range(n)]
    
    def cut(p, n, r):
        if r[n - 1] > 0:
            return r[n - 1]
        if n == 1:
            q = p[0]
        else:
            q = p[n - 1]
            for i in range(1, n):
                q = max(q, p[i - 1] + cut(p, n - i, r))
        r[n - 1] = q
        return r[n - 1] 
    return cut(p, n, r)
    


p = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

print(cut_rod_mem(p, 10))
print(cut_rod_rek(p, 10))