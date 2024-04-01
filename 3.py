import csv


path_to_file = 'astronaut_time.csv'  # путь к файлу с данными
f = open(path_to_file, encoding='utf-8')    # открытие файла
data = list(csv.DictReader(f))  # чтение файла
f.close()
number_station = input()  # получение номера станции
while number_station != 'stop':
    cnt = 0     # счётчик
    for el in data:
        if el['numberStation'] == number_station:
            hour_stop, minute_stop, second_stop = el['timeStop'].split(':')  # получение времени
            time_now = str((int(hour_stop) + int(el['count'])) % 24) + ':' + minute_stop + ':' + second_stop
            ''' time_now - время сейчас на станции'''
            print(
                f'На станции {el["numberStation"]} восстановлено время (время остановки: {el["timeStop"]}). '
                f' Актуальное время: {time_now}')
            cnt += 1
            break
    if cnt == 0:
        print('На этой станции все хорошо')
    number_station = input()  # получение номера станции
