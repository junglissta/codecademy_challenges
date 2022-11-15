def sum_of_prime_factors(n):
  # Write your code here
  Sum = 0
  prime_list = []
  prime_factor_list = []
  for i in range(2,n+1):
    prime = True
    for y in range(2,i):
      if i%y == 0:
        prime = False
    if prime:
      prime_list.append(i)
  x = prime_list[0]
  while x <= n:
    if n%x == 0:
      n = n / x
      prime_factor_list.append(x)

    else:
      x += 1

  Sum = sum(set(prime_factor_list))
  return Sum

print(sum_of_prime_factors(88))