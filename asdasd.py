import random
coef = pow(2, 30)-1

n = random.randint(0, coef)
n = bin(n)[:2]

while (len(str(n)) != 30):
    n= random.randint(0, coef)
    n = bin(n)[:2]
    
print (int(n))
