with open("Txt_python5_3.txt", "r") as salary_string:
    workers = {}
    for line in salary_string:
        line_list = line.split()
        workers[line_list[0]] = int(line_list[-1])
    for family,salary in workers.items():
        if salary <= 20000:
            print(family,salary)
    print(sum(workers.values()) / len(workers.keys()))