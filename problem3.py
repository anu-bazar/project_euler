"""Prime factors of 13195 are 5,7,13,29
Largest prime factor of 600851475143 is?
"""
#### TEST CASE ####
#find possible list of prime numbers until ceiling value
#listing method: list all possible values and find the max
ceiling = 100 #change to desired value
prime = []

for i in range(2,ceiling+1):
    primeOrNot=True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            primeOrNot = False
            break
    if primeOrNot == True:
        prime.append(i)
# print(prime)


#find prime factor
number = 13195 
prime_factor = []
for x in prime:
    if number % x == 0:
        prime_factor.append(x)
# print(prime_factor)
print(max(prime_factor))

#Only works for numbers under 100000, computation for finding prime numbers is not optimal.

#### FASTER VERSION ####
#pickaxe method: throw numbers at it until it's a prime number
# my_number = 13195 
my_number = 600851475143
"""divide until no more for 2, 3 and add by odd numbers"""
while my_number % 2 == 0:
    largest_prime = 2
    my_number = my_number // 2 
factor = 3
while factor * factor <= my_number:
    while my_number % factor == 0:
        largest_prime = factor
        my_number = my_number // factor
    factor += 2 
if my_number > 2:
    largest_prime = my_number
print(largest_prime)

