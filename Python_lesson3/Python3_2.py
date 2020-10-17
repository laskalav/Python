def get_user_data (**kwargs):
    name = kwargs["name"]
    surname = kwargs["surname"]
    year_of_birth = kwargs["year_of_birth"]
    city = kwargs["city"]
    email = kwargs["email"]
    telephone = kwargs["telephone"]
    return print(f"{name}, {surname}, {year_of_birth}, {city}, {email}, {telephone}")


get_user_data(
    name='Иванов',
    surname='Иван',
    year_of_birth='1987',
    city='Нижний Тагил',
    email='i.ivanio@dtagil.ru',
    telephone='+7 987 987 98 79',
)
