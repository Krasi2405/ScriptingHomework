import datetime
import sys

sys.setrecursionlimit(10000)

def fibonacci_generator(max):
    a = 0;
    b = 1;
    for x in range(max):
        if(x % 2 == 0):
            yield a
            a += b
        else:
            yield b
            b += a

def fibonacci_recursion(target, a = 0, b = 1, current = 0, fibonacci_sequence = []):
    if(current == target):
        return fibonacci_sequence
    else:
        if(current % 2 == 0):
            fibonacci_sequence.append(a)
            a += b
        else:
            fibonacci_sequence.append(b)
            b += a
        current += 1
        return fibonacci_recursion(target, a, b, current, fibonacci_sequence)

print("Functions working test: ")
print("Generator: ")
a_list = []
for x in fibonacci_generator(10):
    a_list.append(x)
print(a_list)
print("Recursion: ")

print(fibonacci_recursion(10))

print("Time to calculate 5000th fibonacci number: ")
now = datetime.datetime.now()
for x in fibonacci_generator(5000):
    pass
print("Generator: {}".format(datetime.datetime.now() - now))

now = datetime.datetime.now()
fibonacci_recursion(5000)
print("Recursion: {}".format(datetime.datetime.now() - now))

n = int(input("Which fibonacci number would you like to get?"))
now = datetime.datetime.now()
a_list_2 = []
for x in fibonacci_generator(n):
    a_list_2.append(x)
print()
print("{}th fibonacci number: {}".format(n, a_list_2[n - 1]))
print(datetime.datetime.now() - now)