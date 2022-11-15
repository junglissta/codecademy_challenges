# import numpy
def product_of_the_others(array):
  final_list = []
  for i in array:
    new_list = [x for x in array]
    new_list.remove(i)
    # final_list.append(numpy.prod(new_list))
    prod = 1
    for num in new_list:
      prod = prod * num

    final_list.append(prod)
    new_list.clear()
  return final_list
      
  print(final_list)


print(product_of_the_others([1, 2, 3, 4, 5]))