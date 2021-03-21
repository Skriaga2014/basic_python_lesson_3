'''
1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
2. *(вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу с
числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной. Например:
num_translate_adv("One")
"Один"
num_translate_adv("two")
"два"
'''

# использование google translate API не целесообразно, так как числа переводятся не однотипно:
# 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten' ->
# 'нуль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'Cемь', '8', '9', 'десять'

def num_translate_adv(eng):
    title = True if eng[0].istitle() else False

    en_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    ru_list = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']

    if title:
        eng = eng.lower()

    if eng not in en_list:
        return None

    result = ru_list[en_list.index(eng)]

    if title:
        result = result.title()

    return result

eng_dig = input('Bведите число 0-10 на английском языке: ')
print(num_translate_adv(eng_dig))