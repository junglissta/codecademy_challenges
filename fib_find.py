def fib_finder(n):
  # Initialize variables to store the current and next fibonacci number
  begin = 0
  next = 1
  for i in range(n-1):
    # Calculate the next fibonacci number by adding the current and next numbers
    begin = begin + next
    # Update the current number to be the previous next number
    next = begin - next
  # Return the current fibonacci number, which is the nth number in the sequence
  return begin
print(fib_finder(100))
