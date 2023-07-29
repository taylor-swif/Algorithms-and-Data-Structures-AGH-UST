#f(i, t) = minimalny koszt aby znaleźć się na planecie i z t paliwa. Dla pierwszej planety tankuje do wszystkich t w niej oraz
#jeśli istenieje teleport to go używam. Następnie dla każdej planety od 1 do n - 1, symuluję przylecenie na nią z poprzedniej.
#W pewnym sensie zawsze zatrzymuję się na planecie, lecz nie zawszę korzystam z tankowania. Po symulacji przylecenia
#na aktualna planetę z poprzedniej sprawdzam dla każdego t, czy nie lepiej było przylecieć z t - 1 paliwo i zatankowąć ten 1L.
#Na każdej planecie sprawdzam też możliwość teleportowania się do następnej.
#Na sam koniec zwracam minimalną wartość z ostatniej kolumny (z planety B)
#Złożoność obliczeniowa: O(nE)

from egz1btesty import runtests
from math import inf

def is_teleport(planet, T):

    if planet == T[planet][0]:
        return False
    
    return True

def planets( D, C, T, E ):
    n = len(D)

    F = [[inf for _ in range(n)] for _ in range(E + 1)]
    F[0][0] = 0
    
    if is_teleport(0, T):
        planet = T[0][0]
        cost = T[0][1]
        F[0][planet] = cost

    for fuel in range(1, E + 1):
        F[fuel][0] = F[fuel - 1][0] + C[0]

    
    for planet in range(1, n):
        dist_from_prev_planet =  D[planet] - D[planet - 1]
        max_fuel_possible = E - dist_from_prev_planet

        for fuel in range(max_fuel_possible + 1):
            F[fuel][planet] = min(F[fuel][planet], F[fuel + dist_from_prev_planet][planet - 1])

        for fuel in range(1, E + 1):
            F[fuel][planet] = min(F[fuel][planet], F[fuel - 1][planet] + C[planet])

        if is_teleport(planet, T):
            destination = T[planet][0]
            cost = T[planet][1]
            F[0][destination] = min(F[0][destination], F[0][planet] + cost)


    mini = inf

    for i in range(E + 1):
        if mini > F[i][n - 1]:
            mini = F[i][n - 1]
    
    return mini

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
