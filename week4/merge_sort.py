
def merge(l1,l2):

    if l1 is None:
        return l2
    if l2 is None:
        return l1
    res = []
    top1, top2 = l1.pop(), l2.pop()

    while len(l1) and len(l2):
        if top1 > top2:
            res.append(top1)
            top1 = l1.pop()

        else:

            res.append(top2)
            top2 = l2.pop()
        if l1:
            res.extend(l1)
        else:
            res.extend(l2)

        return res


def sort(ls):
    n = len(ls)
    if n > 1:
        return merge(sort(ls[0:n//2]),sort(ls[n//2:]))
    return ls


print(sort([1,4,13,5,2,7]))