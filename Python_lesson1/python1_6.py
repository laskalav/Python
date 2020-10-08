first_day = 5
last_day = 20
res = 1
while first_day < last_day:
    print(f"{res} - день: {first_day}")
    first_day = first_day + ((first_day / 100) * 10)
    res = res + 1
print(f"На {res}-й день спорстмен достиг результата не менее {last_day} километров.")