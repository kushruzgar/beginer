# Вводится порядковый номер дня недели (1, 2, ..., 7). 
# Вывести на экран его название (понедельник, вторник, среда, четверг, пятница, суббота, воскресенье). 
# Программу реализовать с использованием операторов if-elif.


n = input()

if n == '1':
    print('понедельник')
elif n == '2':
    print('вторник')
elif n == '3':
    print('среда')
elif n == '4':
    print('четверг')
elif n == '5':
    print('пятница')
elif n == '6':
    print('суббота')
else:
    print('воскресенье')
