firms = {}
with open('firmes.txt', 'r') as f:
    for line in f.readlines():
        line = line.split()
        firms[line[0]] = int(line[-2]) - int(line[-1])

profit = [i for i in firms.values() if i > 0]
average_profit = sum(profit)/len(profit)
result = [
    firms,
    {'average_profit': sum(profit)/len(profit)}
]
print (result)
