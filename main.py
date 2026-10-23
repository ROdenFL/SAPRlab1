def fibonachi_function(depth, pre = 1, prepre = 1, count = 1):
    if count >= depth:
        return
    if count == 1:
        print(prepre)
        print(pre)
    nextitem = pre + prepre
    print(str(nextitem))
    fibonachi_function(depth, nextitem, pre, count + 1)

fibonachi_function(11)