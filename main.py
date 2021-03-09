# The formula is: a = bq + r

a = int(input("First number: "))  # Makes input a int
b = int(input("Second number: "))  # Makes input a int
r = a % b  # Takes modulus of a and b
while r:  # Runs until r = 0, when it does we have our GCD

    a = b
    b = r

    r = a % b  # Takes modulus of a and b
print('The GCD is:', b)
