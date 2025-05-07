month_title = ["Январь", "Февраль", "Март", "Апрель",
              "Май", "Июнь", "Июль", "Август",
              "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]

def season_event_description(number_of_months: int):
    month_name = month_title[number_of_months - 1]
    if number_of_months <= 2 or number_of_months > 12:
        event_text = " За окном падал белый снег"
    elif 3 <= number_of_months <= 5:
        event_text = "Птицы пели прекрасные песни"
    elif 6 <= number_of_months <= 8:
        event_text = "Солнце светило ярче чем когда-либо"
    else:
        event_text = "Урожай был невероятным"
    print(f"Вы родились в {month_name}. {event_text}")

season_event_description(int(input("Введите номер вашего месяца рождения: ")))