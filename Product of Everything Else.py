def product_of_the_others(array):
  # Create an empty list to store the products
  final_list = []
  # Iterate through each element in the array
  for i in array:
    # Create a new list which is a copy of the array
    new_list = [x for x in array]
    # Remove the element at the current index from the new list
    new_list.remove(i)
    # Initialize a variable to store the product of the elements in the new list
    prod = 1
    # Iterate through each element in the new list
    for num in new_list:
      # Multiply the product by the current element
      prod = prod * num
    # Append the product to the final list
    final_list.append(prod)
    # Clear the elements in the new list
    new_list.clear()
  # Return the final list of products
  return final_list


print(product_of_the_others([1, 2, 3, 4, 5]))
