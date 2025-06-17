from datetime import datetime

class Task:
    def __init__(self, date_start, date_finish, description):
        self.date_start = date_start
        self.date_finish = date_finish
        self.description = description

tasks = [
    Task("2025-01-01", "2025-01-15", "Проект 1"),
    Task("2025-02-02", "2025-02-16", "Проект 2"),
    Task("2025-03-03", "2025-03-17", "Проект 3"),
    Task("2025-04-04", "2025-04-18", "Проект 4"),
    Task("2025-05-05", "2025-05-19", "Проект 5")
]

latest_task = tasks[0]

for task in tasks:
    if datetime.strptime(task.date_finish, "%Y-%m-%d") > datetime.strptime(latest_task.date_finish, "%Y-%m-%d"):
        latest_task = task

print("Самое позднее занятие:")
print(f"Начало: {latest_task.date_start}")
print(f"Окончание: {latest_task.date_finish}")
print(f"Описание: {latest_task.description}")