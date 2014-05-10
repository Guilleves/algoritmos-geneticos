import random

n = random.randint(0, 90000)

while (len(str(n)) != 30):
    n= random.randint(0, 90000)
    
print n
