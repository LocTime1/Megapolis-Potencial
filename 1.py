path_to_file = 'astronaut_time.csv'  # путь к файлу с данными
path_to_file_2 = 'new_time.txt'   # путь к файлу в котором нужно сохранить данные
f = open(path_to_file, encoding='utf-8')    # открытие файла
d = [i[:-1].split(',') for i in f.readlines()]  # чтение файла в список
del d[0]
f_2 = open(path_to_file_2, encoding='utf-8', mode='w')  # открытие второго файла
cnt = 0     # счётчик
for el in d:
    hour_stop, minute_stop, second_stop = el[3].split(':')  # получение времени
    time_now = str((int(hour_stop) + int(el[4])) % 24) + ':' + minute_stop + ':' + second_stop
    ''' time_now - время сейчас на станции'''
    f_2.write(f'На станции {el[1]} в каюте {el[2]} восстановлено время. Актуальное время: {time_now}\n') # Запись в файл
    if cnt < 3:
        print(f'На станции {el[1]} в каюте {el[2]} восстановлено время. Актуальное время: {time_now}')
        cnt += 1
f.close()
f_2.close()
