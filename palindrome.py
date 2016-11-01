def is_palindrome(number):
    digit_list = []

    while number > 0:
        digit_list.append(number % 10)
        number //= 10
    digit_list_2 = digit_list[len(digit_list)::-1]
    return digit_list == digit_list_2

a_dict = {}

while True:
    num = input("Enter a number or type 'break' to exit the loop.")
    if(num == "break"):
        break
    else:
        num = int(num)
    a_dict[num] = is_palindrome(num)

print(a_dict)