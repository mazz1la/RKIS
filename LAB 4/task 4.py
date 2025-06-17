from datetime import datetime
import locale
locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')

def data_check():
    date_str = input("Введите дату в формате: DD.MM.YYYY: ")
    parts = [int(part.strip()) for part in date_str.split('.')]
    day, month, year = parts
    data_obj = datetime(year, month, day)
    res_str = data_obj.strftime("%A, %d %B, %Y год")
    print(res_str)

data_check()