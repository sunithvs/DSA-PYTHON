def deldup(l):
    ls=[]
    for i in l:
        if l.count(i) == 1:
            ls.append(i)

    return ls
print(deldup([1,2,2,3,4,5,22,2,2,2,2]))