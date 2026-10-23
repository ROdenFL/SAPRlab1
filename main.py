# Функция вывода depth чисел фибоначи подряд начиная с pre и prepre
def fibonachi_function(pre, prepre, count, depth):
    if count >= depth:
        return
    nextitem = pre + prepre # Получение следюущего члена ряда
    print(str(nextitem)) # Вывод в терминал
    fibonachi_function(nextitem, prepre, count + 1, depth) # Рекурсивный вызов функции

fibonachi_function(1, 1, 1, 11)