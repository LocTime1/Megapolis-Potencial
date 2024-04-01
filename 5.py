import csv


path_to_file = 'astronaut_time.csv'  # путь к файлу с данными
f = open(path_to_file, encoding='utf-8')    # открытие файла
data = list(csv.DictReader(f))  # чтение файла в список
sl = {}   # словарь, где ключ - номер станции, а значение - информация о станции
for el in data:
    if el['numberStation'].split('-')[0] not in sl.keys():
        sl[el['numberStation'].split('-')[0][:2]] = [el]
    else:
        sl[el['numberStation'].split('-')[0][:2]].append(el)
for i in sl.keys():
    sum_hours, cnt = 0, 0  # сумма часов простоя и количество астронавтов
    cabins = []   # носера кают
    for el in sl[i]:
        sum_hours += int(el['count'])
        cnt += 1
        cabins.append(el['cabinNumber'])
    print(f'Номер группы: {i}. Каюты: {", ".join(cabins)}. Время простоя: {sum_hours / cnt}')
