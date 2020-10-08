seconds = int(input("Введите время: "))
minutes = seconds // 60
seconds = seconds % 60
hours = minutes // 60
minutes = minutes % 60
print("%02d:%02d:%02d" % (hours, minutes, seconds))

