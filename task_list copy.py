''''Задание

Создайте список, содержащий числа от 2 до 7, выведите его на экран
Добавьте в конец списка строку "Python"
Напечатайте сначала первый потом последний элементы списка
Напечатайте элементы списка со второго по четвертый
Выведите длину списка
Найдите, по какому индексу в списке лежат цифра 6
Удалите из списка строку "Python"'''

newlist = [2, 3, 4, 5, 6, 7]
print(newlist)
newlist.append('Python')
print(newlist[0])
print(newlist[-1])
print(newlist[1: 4])
print(len(newlist))
newlist.index(6)
newlist.remove('Python')