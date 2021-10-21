def is_prime(num):
    """ This function return True if the num is prime else return False"""
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            return False
    return True


def factors(num):
    """ This function returns the factors upto half  """
    for i in range(2,int(num/2)+1):
        if num % i == 0:
            yield i


def primeproduct(m):
    facts = factors(m)
    for i in facts:
        if is_prime(i) and is_prime(m//i):
            return True
    return False


def delchar(s,c):
    if len(c) != 1:
        return s
    lis = []
    for i in list(s):
        if i != c:
            lis.append(i)
    return "".join(lis)


def shuffle(l1,l2):
    lis =[]
    for i,j in zip(l1,l2):
        lis.append(i)
        lis.append(j)
    if len(l1) > len(l2):
        lis += l1[len(l2):]
    else:
        lis += l2[len(l1):]
    return lis
