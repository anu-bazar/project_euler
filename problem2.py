"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
By starting with 1 and 2, the first terms will be:

1, 2, 3, 5, 8, 13, 21, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
find the sum of the even-valued terms.
"""
fibonacci = [1,1]
while (fibonacci[-1]) < 4000000:
    if (len(fibonacci)) < 2:
        fibonacci.append(fibonacci[0])
    elif (len(fibonacci)) >= 2:
        next_number = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(next_number)         
print(sum(fibonacci))
even_fibonacci = []
for x in fibonacci:
    if x % 2 == 0:
        even_fibonacci.append(x)
print(sum(even_fibonacci))
