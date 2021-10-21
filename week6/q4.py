def cubefree(n):
    i = 2
    while n > i**3:
        if n % i**3 == 0:
            return False
        i += 1
    return True

print(cubefree(108))