cashe = {0:0, 1:1}
def Fibo(n):
    if n in cashe:
        return cashe[n]
    else:
        f = Fibo(n - 1) + Fibo(n - 2)
        cashe[n] = f
        return f

for n in [10, 50, 100, 200, 300, 400, 500, 600, 700, 800, 900,1000,1100, 1200, 1250]:
    l = Fibo(n)
    print(l)

