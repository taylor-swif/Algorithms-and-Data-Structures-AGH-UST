from egz2btesty import runtests

def magic( C ):
    n = len(C)
    profit = [-1 for _ in range(n)]
    profit[0] = 0

    for i in range(n-1):
        for j in range(1, 4):
            if profit[i] == -1 or C[i][j][1] == -1:
                continue

            target, enter = C[i][j][1], C[i][j][0]

            chest_gold = C[i][0]
            curr_gold = profit[i]

            if chest_gold <= enter:
                ile_potrzeba = enter - chest_gold
                if ile_potrzeba <= curr_gold:
                    curr_gold -= ile_potrzeba
                    profit[target] = max(profit[target], curr_gold)
            else: #chest_gold > enter
                ile_musze_zabrac = chest_gold - enter
                if ile_musze_zabrac <= 10:
                    curr_gold += ile_musze_zabrac
                    profit[target] = max(profit[target], curr_gold)
                
    return profit[n - 1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
