with open("text_input5_1.txt", "w") as word_string:
    while True:
        lines = input("Введите строку:")
        if not lines:
            break
        word_string.write(lines + "\n")



