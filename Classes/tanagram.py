# Rozwazmy slowa x0x[1] ...x|n - 1] oraz y[0]y[1] ... y|n - 1] skladajace sie z malych liter alfa-
# betu lacinskiego. Takie dwa slowa sa t-anagramem dla t nalezacego od 0 do n - 1, jesli kazdej luterze pierwszego slowa mozna przypisac taka sama litere drugiego slowa,
# znajdujacea sie na pozycji rozniacej sie o najwyzej t, tak ze kazda litera drugiego slowa jest przypisana dokladnie jednej literze slowa pierwszego

# prosze zaimplementowac funkcje
# def tanagram(x, y, t):
#     ...

#     ktora sprawdza czy slowa x i y sa t-anagramami i zwraca True jeśli tak a False w przeciwnym razie. Funkcja powinna byc mozliwie jak najszybsza.

def idx(x):
    return ord(x) - ord('a')


def tanagram(x, y, t):
    n = len(x)
    m = len(y)

    if m != n:
        return False
    
    alf = [0 for _ in range(26)]
    alf_1 = [chr(i + 97) for i in range(26)]
    for i in range(t + 1):

        alf[idx(y[i])] += 1

    left = -t
    rigtt = t
    print(alf)
    print(alf_1)

    for i in range(n):
        if alf[idx(x[i])] >= 1:
           alf[idx(x[i])] -= 1
           if left >= 0:
               alf[left] -= 1
           left += 1
           rigtt += 1 
           if rigtt < n:
            alf[idx(y[rigtt])] += 1
        else:
            return False
    return True

x = "kotomysz"
y = "tokmysoz"
print(tanagram(x, y , 3))
