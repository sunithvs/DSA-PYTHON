pattern = input()
ls = []
line = input()
while line != "":
    if line.__contains__(pattern):
        ls.append(line)
    line = input()

print(ls)

