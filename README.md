# codecademy_challenges
 python code challenges
COMPARATIVE WEIGHTS:
Suppose you had n basketballs, all of them seemingly identical. You are given a balance scale and told that one of the n balls is slightly heavier than the others. What’s the fewest number of times you have to use the scale to find the outlier? You can assume that the scale is very large and able to fit all n balls on each side. Write a scale_of_truth_n() function that takes in the number of basketballs and determines the minimum number of weighs that you’ll need to find the outlier.

For example, if you have 3 balls, you can compare 2 of them to see if they are of equal weight. If they are, then you know the ball that you didn’t weigh is the outlier. On the other hand, if they aren’t of equal weight, then the heavier ball is the outlier. Therefore, scale_of_truth_n(3) should return 1.

FIBBONACI FINDER:
Create a fib_finder() function that finds the nth number in the Fibonacci sequence. As a reminder, the Fibonacci sequence is a mathematical sequence that begins with 0 and 1, with each following term being the sum of the two previous terms.

For example, the first two terms of the sequence are represented by fib_finder(1) and fib_finder(2), which return 0 and 1, respectively. fib_finder(6) should return 5.

PRODUCT OF EVERYTHING ELSE:
Create a product_of_the_others() function that takes in an array of integers and replaces each number in the array with the product of all the numbers in the array except the number at that index itself.

For example, product_of_the_others([1, 2, 3, 4, 5]) should return [120, 60, 40, 30, 24], and product_of_the_others([5, 5, 5]) should return [25, 25, 25].

SEMI-PRIME NUMBERS:
Create a semi_prime_count() function that takes in an integer, n, and returns the count of semi-prime numbers from 1 to n, non-inclusive. A semi-prime number is a number that is the product of two prime numbers. Note that the numbers don’t have to be distinct, meaning that 4 is a semi-prime number since it is 2 * 2.

For example, semi_prime_count() called on 10 should return 3 since there are 3 semi-prime numbers from 1-10 (4, 6, 9). Remember, it’s non-inclusive!

SUM OF PRIME FACTORS:
Create a sum_of_prime_factors() function that takes in an integer n and returns the sum of all of its prime factors. As a reminder, a prime number is a number whose only factors are one and itself. Therefore, a prime factor is a factor of a given number that itself is a prime number.

For example, sum_of_prime_factors(91) should return 20 since its prime factors are 13 and 7.
