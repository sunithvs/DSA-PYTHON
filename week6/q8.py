
def best (ls,num):
    if min(ls) < 0:
        index = list(ls).index(min(ls))
        if sum(ls[:index]) < sum(ls[index:]):










