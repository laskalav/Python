with open(r"C:\Users\LaskaLavr\PycharmProjects\untitled\Python_lesson5\Txt_python5_4.txt", "r", encoding="utf-8") as num_line:
    num_word = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
    num_string = []
    for line in num_line:
        line_list = line.split()
        line_list[0] = num_word[line_list[0]]
        num_string.append(" ".join(line_list))
        # print(line_list)
    print(num_string)
with open("rus_num.txt", "w", encoding="utf-8") as rus_list:
    # for string in num_string:
    #     rus_list.write(string + "\n")
    rus_list.write("\n".join(num_string))