adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""

##  ПЕРЕЗАПИСУЙТЕ зміст змінної adwentures_of_tom_sawer у завданнях 1-3
# task 01 ==
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("\n", " ")

# task 02 ==
""" Замініть .... на пробіл
"""
adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("....", " ")

# task 03 ==
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
while "  " in adwentures_of_tom_sawer:
    adwentures_of_tom_sawer = adwentures_of_tom_sawer.replace("  ", " ")
print("== task 03 ==")
print("Текст після виправлення помилок:", adwentures_of_tom_sawer, "", sep='\n')

# task 04
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
print("== task 04 ==")
print(f"Літера \"h\" зустрічається в тексті {adwentures_of_tom_sawer.count("h")} разів.", "", sep='\n')

# task 05
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
print("== task 05 ==")
words_list = adwentures_of_tom_sawer.split(' ')
words_start_with_capital_counter = 0
for word in words_list:
    if word.istitle():
        words_start_with_capital_counter += 1
print(f"{words_start_with_capital_counter} слів у тексті починається з великої літери.", "", sep='\n')

# task 06
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
target_word = 'Tom'
if target_word in adwentures_of_tom_sawer:
    first_occurrence_index = adwentures_of_tom_sawer.find(target_word)
    if target_word in adwentures_of_tom_sawer[first_occurrence_index + 1::]:
        second_occurrence_index = adwentures_of_tom_sawer.find(target_word, first_occurrence_index + 1)
        message_task06 = f"Слово '{target_word}' знайдене в тексті вдруге на позиції: {second_occurrence_index}"
    else:
        message_task06 = f"Слово '{target_word}' присутнє в тексті лише один раз."
else:
    message_task06 = f"Слово '{target_word}' не знайдене в тексті."
print("== task 06 ==")
print(message_task06, "", sep='\n')

# task 07
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = adwentures_of_tom_sawer.split('.')
# Clean extra spaces in each sentence
for sentence_index in range(len(adwentures_of_tom_sawer_sentences)):
    adwentures_of_tom_sawer_sentences[sentence_index] = adwentures_of_tom_sawer_sentences[sentence_index].strip()
# Clean empty last sentence if exists
if adwentures_of_tom_sawer_sentences[-1] == '':
    adwentures_of_tom_sawer_sentences.pop()

# task 08
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print("== task 08 ==")
print("Четверте речення з тексту:", adwentures_of_tom_sawer_sentences[3], sep='\n')
print("Четверте речення з тексту після переведення в нижній регістр:", adwentures_of_tom_sawer_sentences[3].lower(), "", sep='\n')

# task 09
""" Перевірте чи починається якесь речення з "By the time".
"""
print("== task 09 ==")
target_start_phrase = "By the time"
message_task09 = f"Жодне з речень не починається з фрази \"{target_start_phrase}\""
for sentence_index in range(len(adwentures_of_tom_sawer_sentences)):
    if adwentures_of_tom_sawer_sentences[sentence_index].startswith(target_start_phrase):
        message_task09 = f"Речення {sentence_index + 1} починається з фрази \"{target_start_phrase}\""
print(message_task09, "", sep='\n')

# task 10
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
print("== task 10 ==")
print(f"Кількість символів в останньому речення текста = {len(adwentures_of_tom_sawer_sentences[-1])}.")