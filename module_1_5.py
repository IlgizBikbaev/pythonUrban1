immutable_var = (25, 'книга', ['Виктор Гюго', 'Отверженные'], True)
print('Immutable tuple:', immutable_var)
#immutable_var[1] = 'журнал'
#print(immutable_var)
#кортеж не поддерживает изменение элементов

mutable_list = [4, "Виктор Гюго", 'Иван Бунин', 'Михаил Булгаков', 'Михаил Лермонтов', True]
mutable_list.insert(5,'Уильям Шекспир')
mutable_list.insert(0,5)
mutable_list.pop(1)
print('Mutable list:', mutable_list)

