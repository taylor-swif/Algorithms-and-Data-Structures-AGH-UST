# dynamic algorithm finding n-th fibonacci number
# ofc list isn't obligatory

def fib(n):
    arr = [1 for i in range(n)]
    for i in range(2, n):
        arr[i] = arr[i - 1] + arr[i - 2]
    
    return arr[n-1]

print(fib(10))