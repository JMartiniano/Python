fibonacci =[0,1]
for x in range(int(input())):
    k = int(input())
    if k == 0:
        fibonacci = [0]
    elif k >= 2:
        for i in range (1, k):
           fibonacci += [fibonacci[i]+fibonacci[i-1]]
    print(f'fib({k}) = {(len(fibonacci) - 2) ** 2} calls: {fibonacci[len(fibonacci) - 1 ]}')

