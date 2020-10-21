from random import randint
with open("Txt_python5_5.txt", "w", encoding="utf-8") as number:
    number.write(" ".join([str(randint(0, 100)) for i in range(randint(0, 100))]))
with open("Txt_python5_5.txt", "r", encoding="utf-8") as sum_num:
    sum_lst = sum_num.read()

    sum_lst = sum([int(i) for i in sum_lst.split()])
    print(sum_lst)