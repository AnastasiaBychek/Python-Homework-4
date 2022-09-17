from random import randint
k = 2
coef = []
for i in range(1,4):
    coef.append(randint(2,100))
print(coef)
d = str(f'{coef[0]}x^{k} + {coef[1]}x + {coef[2]} = 0')
print(d)

f= open('my_file.txt', 'w')
f.write(d)