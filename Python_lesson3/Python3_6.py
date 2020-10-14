text = "каждое слово состоит из латинских букв в нижнем регистре"


def int_func(word):
    return word.capitalize()


text_list = text.split(" ")
for index, text_word in enumerate(text_list):
    text_list[index] = int_func(text_word)
print(" ".join(text_list))
