lectures = {}
with open('tabel.txt', 'r',encoding="utf-8") as f:
    for line in f.readlines():
        line_nums = ''.join([i for i in line if i.isdigit() or i == ' '])
        lectures[line.split(':')[0]] = sum([int(i) for i in line_nums.split()])

print(lectures)