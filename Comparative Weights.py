def scale_of_truth_n(n):
  if n < 1:
    return "Error"
  else:
    count = 0
    while n != 1:
      while n % 3 != 0:
        n += 1
      n /= 3
      count += 1
    return count
scale_of_truth_n(-2)