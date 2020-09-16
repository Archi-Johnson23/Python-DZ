max_index = 50
min_index = 20

a = float(input("Введите свой рост(Пример:1.75):"))
b = float(input("Введите свой вес (кг): "))

bmi = round(b / (a**2))
print(f"Ваш результат расчета равен: {bmi}")

before = int((bmi - min_index) / 2)
after = int((max_index - bmi) / 2 - 1)
print(f"{min_index}{'='*before}|{'='*after}{max_index}")
print(' ' * (before + 1), round(bmi))
