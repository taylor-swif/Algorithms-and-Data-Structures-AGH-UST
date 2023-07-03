#Dia kazdego ciagu n liczb mozemy obliczyc k-tadna sume (Zakladamy, Ze k <= n). 
# Poprzez k-ladna sume rozumiemy minimalna sume pewnych liczb wybranch w ten sposöb, 
# ze z kazdych k kolejnych elementow wybralismy prynajmniej jeden z nich 
# (w szczegolnosci oznacza to, ze dia k=1 musimy wybrad wszystkie elementy,
#   a dia k=n wystarczy wybrac jeden, najmniejszy z nich).
# Prosze napisad algorytm, który dia zadanej tablicy liczb naturalnch oraz 
# wartosci k oblicza k ladna sume.

def ksum(A, k):
    n = len(A)
    dp =[float('inf') for _ in range(n)]

    for i in range(k):
        dp[i] = A[i]

    for i in range(k, n):
        minn = float('inf')
        for j in range(1,k):
            minn = min(dp[i - k], minn)
        dp[i] = minn + A[i]
        # dp[i] = min(dp[i - k:i]) + A[i]

    print(dp)
    return min(dp[n - k:n])

k = 4
A = [1, 2, 3, 4, 6 , 15 ,8, 7]

print(ksum(A, k))