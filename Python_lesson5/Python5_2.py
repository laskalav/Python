with open("Txt_python5_2.txt", "r") as count_string:
    string_list = count_string.readlines()
    print(f"Количество строк: {len(string_list)}")
    index = 1
    for word in string_list:
        print(f"Количество слов в строке {index} :{len(word.split())}")
        index += 1
