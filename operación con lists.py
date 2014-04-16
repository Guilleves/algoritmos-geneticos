def fitness(valor, suma):
    return(valor/suma)

a=[100, 200, 400, 600, 300, 900, 100, 200, 300, 500]


total = sum(a)
print total


for i in range(0,10):
    valor = a[i]
    resultado = fitness(valor, total)
    print resultado
