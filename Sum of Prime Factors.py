def sum_of_prime_factors(n):
  # Initialize a variable to store the sum
  Sum = 0
  # Initialize an empty list to store prime numbers
  prime_list = []
  # Initialize an empty list to store prime factors
  prime_factor_list = []
  # Iterate through the range 2 to n+1
  for i in range(2,n+1):
    # Assume i is prime
    prime = True
    # Check if i is divisible by any number in the range 2 to i
    for y in range(2,i):
      if i%y == 0:
        # If i is divisible, set prime to False
        prime = False
    # If i is prime, add it to the list
    if prime:
      prime_list.append(i)
  # Set x to the first prime number in the list
  x = prime_list[0]
  # While x is less than or equal to n
  while x <= n:
    # If n is divisible by x
    if n%x == 0:
      # Divide n by x and store the result in n
      n = n / x
      # Add x to the list of prime factors
      prime_factor_list.append(x)
    # If n is not divisible by x
    else:
      # Increment x by 1
      x += 1
  # Calculate the sum of the unique elements in the list of prime factors
  Sum = sum(set(prime_factor_list))
  # Return the sum
  return Sum


print(sum_of_prime_factors(88))
