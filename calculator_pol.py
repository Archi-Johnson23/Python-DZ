max_index = 50
min_index = 0


name = [(i) for i in input('Введите ваше имя:').split()]
growth = float(input("Введите свой рост(Пример:1.75):"))
weight = float(input("Введите свой вес (кг): "))
age = [(i) for i in input('Введите ваш возраст:').split()]
floor = [(i) for i in input('Введите ваш пол:').split()]

bmi = round(weight / (growth**2))

slovar = dict(Имя=name,
              Рост=growth,
              вес=weight,
              возраст=age,
              пол=floor,)

# Ваше имя: {name} , \nВаш рост {growth}, \nВаш вес {weight},\nВаш возраст {age},\nВаш пол {floor},
print(f"Ваш результат расчета равен: {bmi}")

before = int((bmi - min_index) / 2)
after = int((max_index - bmi) / 2 - 1)
print(f"{min_index}{'='*before}|{'='*after}{max_index}")
print(' ' * (before + 1), round(bmi))

if bmi > 17:
    print('Употребляем меньше пищи,садимся на диету!!!')
else:
    print('Едим больше:жирное,мясо,белок!!! ')


if weight < 50:
    print('Вы слишком худой(ая)')
elif 50 < 100:
    print('Вы упитанный ')


print(slovar)
