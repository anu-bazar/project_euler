"""If we list all Natural numbers below 10 that are multiples of 3 or 5 we get 3,5,6,9. 
The sum of these is 23. Find the sum of all multiples of 3 or 5 below 1000."""
my_numbers = list()
for x in range(1,1000):
    if x%3 == 0 or x%5 == 0:
        my_numbers.append(x)
total_sum = sum(my_numbers)
print(total_sum)