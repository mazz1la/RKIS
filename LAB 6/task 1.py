class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __str__(self):
        return f"Пользователь: {self.login}"

users = [
    User("user_1", "111111"),
    User("user_2", "222222"),
    User("user_3", "333333"),
    User("user_4", "444444"),
    User("user_5", "555555"),
]

login = input("Введите логин: ")
password = input("Введите пароль: ")

for user in users:
    if user.login == login and user.password == password:
        print(f"Авторизация успешна! {user.login}")
        break
else:
    print("Ошибка: пользователь с такими данными не найден")