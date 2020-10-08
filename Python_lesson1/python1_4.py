incoming = abs(int(input("Введите число: ")))
result = 0
while incoming:
    remains = incoming % 10
    incoming = incoming // 10
    if remains > result:
        result = remains
print(result)

