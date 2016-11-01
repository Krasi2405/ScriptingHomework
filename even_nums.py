a_list = []
while True:
    a = input("Enter number or 'break' to exit")
    if a == 'break':
        break
    else:
        a_list.append(int(a))

for x in a_list:
    if x == 237:
        break

    if x % 2 == 0:
        print(x)

