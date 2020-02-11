class Date:
    def __init__(self, str_date):
        self.str_date = str_date

    @classmethod
    def get_date(cls, date):

        d = date[:2]
        m = date[3:5]
        y = date[6:10]
        if cls.check_date(m) == True:
            return f'{int(d)}-{int(m)}-{int(y)}'
        else:
            print(f'Не все элементы являются числами')

    @staticmethod
    def check_date(p):
        month = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
        return True if p.isdigit() and p in month else False


my_date = '15-02-2020'
my = Date.get_date(my_date)
print(my)
