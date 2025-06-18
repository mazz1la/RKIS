class Training:
    def __init__(self, client_id, year, month, duration):
        self.client_id = client_id
        self.year = year
        self.month = month
        self.duration = duration

    def info(self):
        return f"Клиент {self.client_id}, дата {self.month}.{self.year}, Продолжительность {self.duration} мин."

trainings = [
    Training("001", 2025, 1, 15),
    Training("002", 2025, 2, 25),
    Training("003", 2025, 3, 35),
    Training("004", 2025, 4, 45),
    Training("005", 2025, 5, 55)
]

longest = trainings[0]
shortest = trainings[0]

for training in trainings:
    if training.duration > longest.duration:
        longest = training
    if training.duration < shortest.duration:
        shortest = training

print(f"Самая длинная тренировка: {longest.info()}")
print(f"Самая короткая тренировка: {shortest.info()}")