
"""
Write a program that prints the numbers from 1 to 20. 
But for multiples of three print “Fizz” instead of the number 
and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.
"""

def get_fizzbuzz(i: int):
    if i % 3 == 0:
        return 'Fizz'
    if i % 5 == 0:
        return 'Buzz'
    if (i % 3 == 0) and (i % 5 == 0):
        return 'FizzBuzz'

def play_fizzbuzz():
    for i in range(20):
        fizzbuzz_str = get_fizzbuzz(i)
        print(fizzbuzz_str)

play_fizzbuzz()