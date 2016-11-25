import random

cows = 0
bulls = 0
number = random.randint(1000, 10000)
number = 3505
print(number)
while True:
    response = input("Enter a guess: ")

    if (int(response) == number):
        break

    response_list = list(response)
    number_list = list(str(number))
    value_map = {}

    for x in response_list:
        value_map[x] = 0
        for y in number_list:
            if(x == y):
                value_map[x] += 1

    for x, y in zip(response_list, number_list):
        if(x == y):
            bulls += 1

        if x in number_list and value_map[x] > 0:
            cows += 1
            value_map[x] -= 1

    cows -= bulls
    if(cows < 0):
        cows = 0

    print("Bulls: {}".format(bulls))
    print("Cows: {}".format(cows))

    bulls = 0
    cows = 0

print("You win!.")