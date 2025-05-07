from datetime import datetime
current = datetime.today()
day = current.strftime("%A")
month = current.strftime("%B")
name = ("Vlad")
print(f"{day}\n{month}\n{name}")