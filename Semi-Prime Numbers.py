def semi_prime_count(n):
  # Initialize an empty list
  listl = []
  # Initialize another empty list
  list_final = []
  # Iterate through the range 2 to n
  for i in range(2,n):
    # Assume i is prime
    prime = True
    # Check if i is divisible by any number in the range 2 to i
    for y in range(2,i):
      if i%y == 0:
        # If i is divisible, set prime to False
        prime = False
    # If i is prime, add it to the list
    if prime:
      listl.append(i)
  # Iterate through the list of prime numbers
  for left in listl:
    # Iterate through the list of prime numbers again
    for right in listl:
      # If the product of the two numbers is less than n
      if (left * right) < n:
        # Add the product to the final list
        list_final.append((left * right))
        
  # Return the number of unique elements in the final list
  return len(list(dict.fromkeys(list_final)))


print(semi_prime_count(10))
