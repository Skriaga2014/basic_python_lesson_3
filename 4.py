'''
4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки в формате
«Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий, а значения — словари,
реализованные по схеме предыдущего задания и содержащие записи, в которых фамилия начинается с соответствующей буквы.
Например:
thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
{
    "А": {
        "П": "Петр Алексеев"
    },
    "С": {
        "И": ["Иван Сергеев", "Инна Серова"],
        "А": ["Анна Савельева"]
    }
}
'''

def thesaurus_adv(names_list):
    result_dict = {}
    for i in names_list:
        fio = i.split(' ')
        name_1 = fio[0][0]
        surname_1 = fio[1][0]
        if surname_1 in result_dict:
            if name_1 in result_dict[surname_1]:
                result_dict[surname_1][name_1].append(i)
            else:
                result_dict[surname_1][name_1] = [i]
        else:
            result_dict[surname_1] = {name_1: [i]}

    return result_dict

names_list = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]
print(names_list)
names_dict = thesaurus_adv(names_list)
print(names_dict)
print(names_dict['С']['И'])

print('\nдля сортировки по ключам потребуется преобразование словаря в список')