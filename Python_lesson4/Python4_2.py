source_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

result = [
    n  # Результат, который идёт в лист
    for i, n in enumerate(source_list)  # достаём переменные i и n из списка туплей возращаемых из enumerate
    if source_list[i] > source_list[i-1] and i != 0  # Проверяем условия, пропуская нулевой индекс
]
print(result)
