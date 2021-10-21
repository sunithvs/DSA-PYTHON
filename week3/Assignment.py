def expanding(lis):
    minimum = lis[0]-lis[1]
    for li in lis[1:-1]:
        dif = abs(li - lis[lis.index(li)+1])
        print(dif)
        if minimum >= dif:
            return False
        minimum = dif
    return True

