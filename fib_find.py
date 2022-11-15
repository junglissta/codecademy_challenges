def fib_finder(n):
  # Write your code here
  begin = 0
  next = 1
  for i in range(n-1):
    begin = begin + next
    next = begin - next
  return begin
print(fib_finder(100))