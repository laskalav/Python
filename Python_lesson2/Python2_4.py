string = input("Введите предложение: ")
string_list = string.split(' ')
for index, word in enumerate(string_list):
    print(f"{index} {word[:10]}")
