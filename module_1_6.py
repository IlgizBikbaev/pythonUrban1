my_dict = {"Шагреневая кожа": 1831, 'Евгения Гранде': 1833, 'Отец Горио': 1835, 'Тридцатилетняя женщина': 1842}
print('Моя библиотека Оноре де Бальзака: ', my_dict)
# Вывеcти на экран значение по ключу
book_ = my_dict.get('Отец Горио')
print('Год выхода романа: ', book_)
#Добавить две произвольные пары в словарь my_dict
my_dict.update({'Гобсек': 1830, 'Блеск и нищета куртизанок': 1847})
print('Обновленная библиотека после покупки: ', my_dict)
#Удалить пару в словаре по ключу из словаря my_dict и вывести её значение на экран
a = my_dict.pop('Гобсек')
print('Год выхода романа, отданного другу на прочтение:', a)
print('Сейчас у меня: ', my_dict)

my_set = {'д','o','б','р','o', 1, 2, 3, 4, 5}
print(my_set)
#Добавить 2 элемента в множество my_set
my_set.update(['т', 6])
#Удалить элемент из множества my_set
my_set.remove('o')
print(my_set)
