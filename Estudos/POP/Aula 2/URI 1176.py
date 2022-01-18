fibonacci = [0, 1]
for x in range(int(input())):
    n = int(input())
    if (n == 0):
        fibonacci = [0]
    elif (n >= 2):
        fibonacci = [0, 1]
        for i in range(1, n):
            fibonacci += [fibonacci[i]+fibonacci[i-1]]
    print(f'Fib({n}) = {fibonacci[len(fibonacci)-1]}')