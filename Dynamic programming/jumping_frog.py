# Pewna zaba skacze po osi liczbowej. Ma sie dostaé z zera do n - 1, skaczac wylacznie w kierunku wiekszych liezb. 
# Skok z liczby i do liczby i (j > i) kosztuje ja j - i jednostek energi, a jej energia nigdy nie moze spasc ponizej zera. 
#  Na poczatku zaba ma 0 jednostek energi, ale na szczescie na niektórych liczbach takze na zerze leza przekaski o okreslonej
#  wartosci energetycznei (wartosc przekaki dodaje sie do aktualnej energii Zbigniewa). Prosze zaproponowac algorytm, 
# który oblicza minimalna liezbe skoków potrzebna na dotarcie z O do n - 1 mając dana tablice A z wartosciami energetycznymi 
# przekasek na kazdej z liczb

def frog(A):
    n = len(A)
    F = [[float('inf') for _ in range(n)] for _ in range(n)]

    for j in range(n):
        F[j][0] = 0
    # F[i][j]   i - tyle mam paliwa
    #           j - jestem na tym polu
    for i in range(A[0], 0, -1): 
        F[A[0] - i][i] = 1

    for i in range(n):
        for j in range(1, n):# koloejne pola z których skaczę 
            if F[i][j] < float('inf'): # jezeli tam doskoczyłem
                energy = min(A[j] + i, n - 1 - j) # ograniczenie od góry
                for k in range(energy):
                    next_j = j + energy - k
                    F[k][next_j] = min(F[k][next_j], F[i][j] + 1)
    
    print(*F, sep='\n')
    return F[0][n - 1]

A = [2, 2, 1, 0, 0, 0]
print(frog(A))