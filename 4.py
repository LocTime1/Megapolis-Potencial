path_to_file = 'astronaut_time.csv'  # путь к файлу с данными
path_to_file_2 = 'station_max_downtime.csv'   # путь к файлу в котором нужно сохранить данные
f = open(path_to_file, encoding='utf-8')    # открытие файла
d = [i[:-1].split(',') for i in f.readlines()]  # чтение файла в список
del d[0]

sl = {}   # словарь, где ключ - номер станции, а значение - информация о станции
for i in d:
    sl[i[1]] = i
stop_9 = []   # список со станциями, где время простоя равно 9
for i in sl.keys():
    if sl[i][4] == '9':
        stop_9.append(sl[i])
f_2 = open(path_to_file_2, mode='w', encoding='utf-8')  # открытие файла
f_2.write('WatchNumber,numberStation,cabinNumber,timeStop,count\n')
f_2.writelines([','.join(i) + '\n' for i in stop_9])  # Запись в файл
f.close()
f_2.close()
