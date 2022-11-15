def semi_prime_count(n):
  listl = []
  list_final = []
  for i in range(2,n):
    prime = True
    for y in range(2,i):
      if i%y == 0:
        prime = False
    if prime:
      listl.append(i)
  for left in listl:
    for right in listl:
      if (left * right) < n:
        list_final.append((left * right))
        
  return len(list(dict.fromkeys(list_final)))
  

print(semi_prime_count(10))