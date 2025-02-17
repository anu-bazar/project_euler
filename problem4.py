"""A palindromic number reads the same both ways. The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 x 99 
Find the largest palindrome made from the product of two 3 digit numbers
"""

def is_palindrome(number):
    """Takes number checks for palindrome"""
    my_list = list(str(number))
    half_length = len(my_list) // 2 

    # Divide into two halves so we can do comparison directly
    first_half = []
    second_half = []
    for i in range(0, half_length):
        first_half.append(my_list[i])
    for j in range(len(my_list) - 1, half_length - 1, -1):
        second_half.append(my_list[j])

    # Check for palindrome
    if first_half == second_half:
        # print('Palindrome')
        return True
    else:
        # print('Not Palindrome')
        return False

#The largest palindrome made from the product of two 2 digit numbers is 9009 = 91 x 99.
contenders = []
pair = []
#Take the 90-100 range or 900-1000 range (top 10% highest values)
for x in range(900,1000):
    for y in range(900,1000):
        # pair them up
        product = x*y
        if is_palindrome(product) == True:
            #append if palindrome
            contenders.append(product)
            pair.append((x, y))
#extract max value
max_palindrome = max(contenders)
max_pair = pair[max_index]
print(max_palindrome, max_pair)