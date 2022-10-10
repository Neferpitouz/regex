from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv


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


with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    for lists in contacts_list:
        fio_sorting(lists)
        print(lists)
    contacts_list = regs_sorting(contacts_list)




# pprint(contacts_list)
pprint(contacts_list)
