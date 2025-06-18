class Training:
    def __init__(self, id, year, month, mins):
        self.id = id
        self.year = year
        self.month = month
        self.mins = mins

all_trainings = [
    Training("001", 2022, 1, 35),
    Training("002", 2022, 2, 45),
    Training("003", 2023, 3, 55),
    Training("004", 2023, 4, 65),
    Training("005", 2024, 5, 75),
    Training("006", 2024, 6, 85),
    Training("007", 2024, 7, 95),
    Training("008", 2025, 8, 105),
    Training("009", 2025, 9, 115),
    Training("010", 2025, 10, 125)
]

year_mins = {}

for training in all_trainings:
    if training.year in year_mins:
        year_mins[training.year] += training.mins
    else:
        year_mins[training.year] = training.mins

best_year = 0
max_mins = 0

for year, duration in year_mins.items():
    if duration > max_mins or (duration == max_mins and year < best_year):
        best_year = year
        max_mins = duration

print(f"Самый активный год: {best_year}")
print(f"Всего тренировались: {max_mins} минут")