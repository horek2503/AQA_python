# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
alice_in_wonderland = '''"Would you tell me, please, which way I ought to go from here?"
"That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
'''

# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
print("Task02:")
for current_symbol in alice_in_wonderland:
    if current_symbol == "'":
        print(current_symbol)
print("")

# task 03 == Виведіть змінну alice_in_wonderland на друк
print("Task03:", alice_in_wonderland, sep='\n')

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea_area = 436402
azov_sea_area = 37800
message_task04 = f'''Площа Чорного моря становить: {black_sea_area:,} км2.
Площа Азовського моря становить {azov_sea_area:,} км2.
Сумарна площа обох морів складає {black_sea_area + azov_sea_area:,} км2.
'''
print("Task04:", message_task04, sep='\n')

# task 05
"""Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
items_total = 375291
items_warehouses_01_02 = 250449
items_warehouses_02_03 = 222950
items_warehouse_01 = items_total - items_warehouses_02_03
items_warehouse_02 = items_warehouses_01_02 - items_warehouse_01
items_warehouse_03 = items_total - items_warehouses_01_02
message_task05 = f'''На першому складі розміщено {items_warehouse_01:,} товарів.
На другому складі розміщено {items_warehouse_02:,} товарів.
На третьому складі розміщено {items_warehouse_03:,} товарів.
'''
print("Task05:",message_task05, sep='\n')

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
monthly_payment = 1179
installments_months = 18
message_task06 = f"Вартість комп'ютера при оплаті {monthly_payment}грн щомісяця протягом {installments_months}міс. складе {monthly_payment * installments_months}грн."
print("Task06:",message_task06, "", sep='\n')

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
message_task07 = f"""Залишок від ділення чисел складає:
a) 8019 : 8 -> {8019 % 8}
b) 9907 : 9 -> {9907 % 9}
c) 2789 : 5 -> {2789 % 5}
d) 7248 : 6 -> {7248 % 6}
e) 7128 : 5 -> {7128 % 5}
f) 19224 : 9 -> {19224 % 9}
"""
print("Task07:",message_task07, sep='\n')

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
items = [
    {'name': 'Піца велика', 'qty': 4,'price': 274},
    {'name': 'Піца середня', 'qty': 2,'price': 218},
    {'name': 'Сік', 'qty': 4,'price': 35},
    {'name': 'Торт', 'qty': 1,'price': 350},
    {'name': 'Вода', 'qty': 3,'price': 21}
]
total_amount = 0
print("Task08:")
for item in items:
    item_amount = float(item['qty']) * float(item['price'])
    print(f'Вартість "{item['name']}" = {item_amount}грн;')
    total_amount += item_amount
print(f"Загальна вартість: {total_amount}грн;\n")

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos_qty = 232
photos_per_page = 8
if photos_qty % photos_per_page:
    pages_number = photos_qty // photos_per_page + 1
else:
    pages_number = photos_qty // photos_per_page
message_task09 = f"Ігорю знадобиться {pages_number} сторінок в альбомі щоб вклеїти всі свої {photos_qty} фотографії.\n"
print("Task09:",message_task09, sep='\n')

# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
distance = 1600
fuel_consumption = 9
fuel_tank_capacity_full = 48
total_fuel_needed = distance / 100 * fuel_consumption
# We can set minimal tank fuel level (in real life we cannot drive to 0 liters left in a tank)
minimal_fuel_level = 0
# Calculate usable fuel tank capacity considering minimal fuel level
fuel_tank_capacity_usable = fuel_tank_capacity_full - minimal_fuel_level
if total_fuel_needed % fuel_tank_capacity_usable:
    gas_station_visits = int(total_fuel_needed // fuel_tank_capacity_usable + 1)
else:
    gas_station_visits = int(total_fuel_needed // fuel_tank_capacity_usable)
message_task10 = f"Щоб подолати {distance}км з баком {fuel_tank_capacity_full}л і розходом палива {fuel_consumption}л/100км потрібно {gas_station_visits} разів відвідати АЗС.\n"
print("Task10:",message_task10, sep='\n')