def sort(lis):

    for i in range(len(lis)):
        for j in range (1,len(lis)-i):
            if lis[j][1] == lis[j-1][1]:
               if lis[j][0] < lis[j - 1][0]:
                lis[j], lis[j - 1] = lis[j - 1], lis[j]
            elif lis[j][1] < lis[j-1][1]:
                lis[j], lis[j - 1] = lis[j - 1], lis[j]

    return lis


def histogram(lis):
    res = []
    items = set(lis)
    for item in items:
        res.append((item, lis.count(item)))
    res = sort(res)
    return res


def getcourse(code,courses):
    for course in courses:
        if course[0] == code:
            return course[1]


def getGrades(student, courses, grades):

    res = []
    for grade in grades:
        if grade[0] == student[0]:
            res.append((grade[1], getcourse(grade[1], courses), grade[2]))

    res = sorted(res, key=lambda x:x[0])
    return res


def transcript(courses, students, grades):
    res = []
    students = sorted(students, key=lambda x:x[0])
    for student in students:
        res.append((student[0], student[1], getGrades(student, courses, grades)))
    return res

print(transcript([("T1","Test 1"), ("T2","Test 2"), ("T3","Test 3")], [("Opener","Rohit Sharma"),("Captain","Virat Kohli"),("No3","Cheteshwar Pujara")],[("Opener","T1","14"),("Captain","T1","33"),("No3","T1","30"),("Opener","T2","55") ,("Captain","T2","158"),("No3","T2","19"), ("Opener","T3","33"),("Captain","T3","95"),("No3","T3","51")]))