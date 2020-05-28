"""
Programming Practice: Determining prime Number.
In this program read a positive integer and determine if
it is a prime number. Definition of prime number: Not divisible
by any other than one and itself. For example, it is a prime
number because it is only divisible by one and two.
The number 1 is not prime because it is divisible by 2 and 2,
except 1 and 2.
If the prime number is in the output, print the prime statement and if it is not the prime number, print the not prime statement. Please note that the output is exactly as stated. Small letters are important.
Sample input:
25
Sample output:
not prime

"""

num = int(input())
max_prime = {}
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("not prime")
            break
    else:
        count = 0
        for i in range(2, num):
            if i % 2 == 0:
                count += 1
        max_prime = max_prime + {num:count}

        print("prime")
else:
    print("not prime")
