rating_list = [7, 5, 3, 3, 2]
user_rating = int(input("Введите свой рейтинг: "))
rating_list.append(user_rating)
rating_list.sort(reverse=True)
print(rating_list)
