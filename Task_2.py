def prime_facs(n):
   i = 2
   factors = []
   while i * i <= n:
       while n % i == 0:
           factors.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       factors.append(n)
   return factors

print(prime_facs(int(input())))