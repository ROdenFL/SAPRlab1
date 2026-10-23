def fibonachi_function(pre, prepre, count, depth):
    if count >= depth:
        return
    nextitem = pre + prepre
    print(str(nextitem))
    fibonachi_function(nextitem, prepre, count + 1, depth)

fibonachi_function(1, 1, 1, 11)