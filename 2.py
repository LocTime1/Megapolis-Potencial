import csv


path_to_file = 'astronaut_time.csv'  # путь к файлу с данными
f = open(path_to_file, encoding='utf-8')    # открытие файла
data = list(csv.DictReader(f))  # чтение файла

for i in range(1, len(data)):     # сортировка вставками
    j = i - 1
    key = data[i]
    while key['cabinNumber'][3:] < data[j]['cabinNumber'][3:] and j >= 0:
        data[j + 1] = data[j]
        j -= 1
    data[j + 1] = key
cnt = 0     # счётчик
for el in data:
    hour_stop, minute_stop, second_stop = el['timeStop'].split(':')  # получение времени
    time_now = str((int(hour_stop) + int(el['count'])) % 24) + ':' + minute_stop + ':' + second_stop
    ''' time_now - время сейчас на станции'''
    print(f'На станции {el["numberStation"]} в каюте {el["cabinNumber"]} восстановлено время. Актуальное время:'
          f' {time_now}')
    cnt += 1
    if cnt == 3:
        break
f.close()
