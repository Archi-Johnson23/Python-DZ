# исходная строка
a = ('Не знаю,как там в Лондоне,я не была.Может,там собака - друг человека.А у нас управдом - друг человека.')

# 1)подсчитать количество символов

print('количество симолов -' , len(a))

# 2)развернуть строку
print(a[:])

# 3) сделать каждое слово с большой буквы
print(a.title())

# 4)весь текст прописными буквами
print(a.lower())

# 5)число вхождений
count = a.count(('нд'))
print(('нд'),',','число вхождений' ,count )

count = a.count(('ам'))
print(('ам'),',','число вхождений' ,count )

count = a.count(('о'))
print(('о'),',','число вхождений' ,count )


# 6) упражнения для себя
print(a + ('Hello World!!!'))
print(a.split())
print(a * 5) #умножить текст в 5 раз
print(a[::-1])
print(a[3:7]) #знаю