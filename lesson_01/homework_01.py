# task 01 == Виправте синтаксичні помилки
print("Hello", end = " ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03 == Вcтавте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimetry = storona_1 + storona_2 + storona_3 + storona_4
print(f"Периметр фігури з task 05 дорівнює: {perimetry}")


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apple_trees = 4
pear_trees = apple_trees + 5
plum_trees = apple_trees - 2
total_trees = apple_trees + pear_trees + plum_trees
print("Яблунь посадили ", apple_trees,end="; ")
print("Груш посадили ", pear_trees,end="; ")
print("Слив посадили ", plum_trees, end='.\r\n' )
print("Всього дерев посадили: ", total_trees)

# task 08
"""
До обіду температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
morning_temperature = 5
noon_temperature = morning_temperature - 10
evening_temperature = noon_temperature + 4
print(f"Зранку температура була {morning_temperature} градусів; В обід стала {noon_temperature} градусів.")
print(f"Температура ввечері піднялась на 4 градуси і становила: {evening_temperature} градус.")

# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скільки сьогодні дітей у театральному гуртку?
"""
boys_total = 24
girls_total = boys_total // 2
print(f"В гуртку займається {boys_total} хлопчиків і {girls_total} дівчаток.")
print(f"Але сьогодні в гуртку присутні загалом {boys_total - 1 + girls_total - 2} дітей")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дороже,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book_price = 8.0
second_book_price = first_book_price + 2
third_book_price = (first_book_price + second_book_price) / 2
print(f"Перша, друга та третя книжки коштують по {first_book_price}, {second_book_price} та {third_book_price} грн відповідно.")
print(f"Загальна вартість книжок по одному примірнику складає: {first_book_price + second_book_price + third_book_price} грн")
