result = 0

while True:
    incoming = input('Enter number or "q" for exit: ')

    num_list = incoming.split(' ')

    for num in num_list:
        if num.isdigit():
            result += int(num)
        elif num == 'q':
            break

    print(result)

    if 'q' in num_list:
        break
