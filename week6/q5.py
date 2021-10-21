def listdiff(l1,l2):
    ldiff1 = []
    ldiff2 = []
    for i in l1:
        if i not in l2:
            ldiff1.append(1)
    for i in l2:
        if i not in l1:
            ldiff2.append(i)
    return (ldiff1,ldiff2)

print(listdiff([2,4,2],[4,2,2,3,1,4]))