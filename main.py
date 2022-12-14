from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re


def fio_sorting(names_list):
    fio = 0
    while fio < 3:
        temp = names_list[fio].split()
        leng_temp = len(names_list[fio].split())
        count = 0
        if leng_temp >= 2:
            while count < leng_temp:
                names_list[fio] = temp[count]
                count += 1
                fio += 1
            if leng_temp == 3:
                break
        fio += 1
    return names_list


def regs_sorting(data_lists):
    for list_comp in data_lists:
        for list_comp2 in data_lists:
            if len(list_comp) == 8:
                listcomp = list_comp.pop(7)
            if list_comp[0] == list_comp2[0] and list_comp[1] == list_comp2[1]:
                for i in range(0, 7):
                    if len(list_comp[i]) < len(list_comp2[i]):
                        list_comp[i] = list_comp2[i]
                    else:
                        list_comp2[i] = list_comp[i]
    list_no_doubles = []
    for list_reg in data_lists:
        if list_reg not in list_no_doubles:
            list_no_doubles.append(list_reg)
    return list_no_doubles


def regex_numbers(data):
    pattern = r'(\+7|8)\s*\(?(\d{3})\)?\D*(\d{3})\D*(\d{2})\D*(\d{2})'
    subst = r'+7(\2)\3-\4-\5'
    pattern2 = r'(\(?)(\w{3}\.\D{1}\d{4})(\)?)'
    subst2 = r'\2'
    result = re.sub(pattern, subst, data)
    result = re.sub(pattern2, subst2, result)
    return result


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    for lists in contacts_list:
        fio_sorting(lists)
        print(lists)
    contacts_list = regs_sorting(contacts_list)
    for lists in contacts_list:
        lists[5] = regex_numbers(lists[5])

# pprint(contacts_list)
pprint(contacts_list)
# (\+7|8)\s*\(?(\d{3})\)?\D*(\d{3})\D*(\d{2})\D*(\d{2})
# +7(\2)\3-\4-\5

# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)
