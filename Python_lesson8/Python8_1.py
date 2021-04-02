import datetime


class Date(object):
    def __init__(self , date_string):
        self.date_string = date_string

    @classmethod
    def num_date(cls, int_date):
        int_date = str(int_date)
        return [int(i) for i in int_date.split("-")]

    @staticmethod
    def val_date(day, month, year):
        if day > 31 or month > 12 or year < 0:
            print("Incorrect date")
            return False
        else:
            return True


if __name__ == '__main__':
    date = Date.num_date(int_date=datetime.date.today())
    d = datetime.date.today()
    valid_date = Date.val_date(day=d.day,
                               month=d.month,
                               year=d.year)
    print(date)
    print(valid_date)


