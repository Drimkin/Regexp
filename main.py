from pprint import pprint
import csv
import re

# Читаем адресную книгу в формате CSV в список contacts_list:

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# pprint(contacts_list)
# 1. Выполните пункты 1-3 задания.
# Ваш код
new_contacts_list = []
for contact in contacts_list:
    # Создаем регулярку по телефонным номерам и приводим телефоны в правильный вид
    pattern = r"(\+7|8)?\s*\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})(\s*)\(?(доб\.?)?\s*(\d*)?\)?"
    contact[5] = re.sub(pattern, r"+7(\2)\3-\4-\5 \7\8", contact[5])
    #pprint(contact)
    # Разделяем Имя, Фамилия, Отчество
    contact[:3] = " ".join(contact[:3]).split()
    # Проверям указано или нет отчество, если нет добавляем место
    if contact[2] == "":
        contact.insert(2, "")
    #pprint(contact)
    new_contacts_list.append(contact)

# pprint(new_contacts_list)
# Проверяем есть ли совпадения по Фамилии и Имени, если есть объединяем данные
i = 0
while i < len(new_contacts_list):
    j = i + 1
    while j < len(new_contacts_list):
        if new_contacts_list[i][:2] == new_contacts_list[j][:2]:
            for x in range(len(new_contacts_list[i])):
                if not new_contacts_list[i][x] and new_contacts_list[j][x]:
                    new_contacts_list[i][x] = new_contacts_list[j][x]
            new_contacts_list.remove(new_contacts_list[j])
        else:
            j += 1
    i += 1
# pprint(new_contacts_list)


# 2. Сохраните получившиеся данные в другой файл.
# Код для записи файла в формате CSV:
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')

#  Вместо contacts_list подставьте свой список:
    datawriter.writerows(new_contacts_list)