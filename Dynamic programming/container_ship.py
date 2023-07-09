# W porcie na odbiór oczekuje n kontenerów z towarem. Waga każdego kontenera jest znana i zapisana w tablicy T (w kilogramach). Dwuczęściowy kontenerowiec, który przypłynął odebrać towar jest ogromny - na tylko jednej z jego części zmieściłyby się wszystkie oczekujące kontenery. Jednak ze względów technicznych, aby statek nie zatonął, w każdej z dwóch jego części musi znajdować się towar o tej samej łącznej wadze. Z tego względu władze portowe muszą zaopatrzyć statek w pewną ilość kilogramowych odważników, które pozwolą na wyrównanie wagi w obydwu jego częściach. Odważniki te jednak są drogie, więc zależy im na tym, aby użyć ich jak najmniej. Twoim zadaniem jako programisty jest napisanie programu, który policzy, jaka jest ta najmniejsza możliwa liczba odważników.
# Algorytm należy zaimplementować jako funkcję postaci:
# def kontenerowiec( T ):
#   ...
# która przyjmuje tablicę wag kontenerów T i zwraca najmniejszą konieczną liczbę odważników, które trzeba umieścić na statku.
# Przykład. Dla danych: T = [1, 6, 5, 11]
# Wynikiem jest liczba 1


def container_ship(T):
    n = len(T)
    sum = [0 for _ in range(n)]
    sum[0] = T[0]

    for i in range(1, n):
        sum[i] = sum[i - 1] + T[i]
    dp = [[float('inf') for _ in range(sum[n - 1] + 1)] for _ in range(n)]

    dp[0][T[0]] = 1
    dp[0][0] = 1

    for i in range(1, n):
        for j in range(sum[n - 1] + 1):
            if dp[i - 1][j] == 1:
                x=j + T[i]
                y=sum[i] - j
                dp[i][j + T[i]] = 1
                dp[i][sum[i] - j] = 1

    minn = float('inf')
    for j in range(sum[n - 1] + 1):
        if dp[n - 1][j] == 1:
            a = j
            b = sum[n - 1] - j

            minn = min(minn, abs(a - b))
    return minn

T = [1, 6, 5, 11]

print(container_ship(T))