# Функция вывода depth чисел фибоначи подряд начиная с pre и prepre
def fibonachi_function(depth, pre = 1, prepre = 1, count = 1):
    if count >= depth:
        return
    if count == 1:
        print(prepre)
        print(pre)
    nextitem = pre + prepre # Получение следюущего члена ряда
    print(str(nextitem)) # Вывод в терминал
    fibonachi_function(depth, nextitem, pre, count + 1) # Рекурсивный вызов функции

fibonachi_function(11)