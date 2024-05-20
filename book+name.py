# На вход программы подаются строки (названия книг). 
# В программе уже реализовано их чтение и сохранение в списке (каждый элемент - название книги). 
# После этого, из полученного списка нужно удалить все названия, состоящие из двух и более слов (слова разделяются пробелом). 
# Результат выведите на экран в виде строки из оставшихся названий через пробел.


import sys

# считывание списка из входного потока
lst_in = list(map(str.strip, sys.stdin.readlines()))

lst_out = []
i = 0
while i < len(lst_in):
    if len(lst_in[i].split()) == 1:
        lst_out.append(lst_in[i])
    i += 1
        
print(*lst_out)
