# ewien przedsiębiorca potrzebuje zamówić do swojej firmy dywany o łącznym polu powierzchni wynoszącym N metrów kwadratowych. Nie martwi się on jakich będą one wymiarów, ponieważ może je w dowolny sposób przycinać i łączyć. Aczkolwiek sklep, w którym chce je kupić, sprzedaje tylko kwadratowe dywany o boku długości wyrażoną liczbą naturalną określającą długość w metrach. Koszt zapakowania każdego dywanu jest stały niezależnie od jego wielkości. Ze względów podatkowych przedsiębiorca potrzebuje zminimalizować łączny koszt zapakowania dywanów, które zakupi, jednocześnie dbając o środowisko nie może dopuścić, żeby jakikolwiek fragment dywanu się zmarnował. Twoim zadaniem jako jego pracownika jest stworzenie listy wymiarów dywanów (wyrażonych jako długość ich boku w metrach), które przedsiębiorca musi zakupić.
# Algorytm należy zaimplementować jako funkcję postaci:
# def dywany( N ):
#   ...
# która przyjmuje wymagane pole powierzchni dywanów N w metrach kwadratowych, a zwraca tablicę długości boków dywanów, które trzeba kupić.
# Przykład. Dla danych: N=6
# Wynikiem jest np. tablica [1, 1, 2]

def carpet(N):
    dp = [float('inf') for _ in range(N + 1)]
    dp[0] = 0
    dp[1] = 1
    
    for i in range(2, N + 1):
        j = 1
        while i >= j * j:
            dp[i] = min(dp[i - 1], dp[i - j*j]) + 1
            j += 1
    print(dp)
    return dp[N]

print(carpet(18))
