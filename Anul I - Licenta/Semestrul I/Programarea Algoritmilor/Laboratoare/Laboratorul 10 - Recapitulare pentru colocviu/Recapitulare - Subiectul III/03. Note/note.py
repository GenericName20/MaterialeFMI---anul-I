# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/note.in"

inputFileName = "note.in"

def getInput():
    catalog = {}
    with open(inputFileName, "r") as f:
        studentsCount, coursesCount = [int(var) for var in f.readline().split()]
        for _ in range(studentsCount):
            studentName = f.readline().strip()
            catalog[studentName] = {}
            for _ in range(coursesCount):
                courseName, *grades = f.readline().strip().split(",")
                grades = [int(grade) for grade in grades]
                catalog[studentName][courseName] = grades

    return catalog

def despre_elev(catalog, studentName):
    stats = []
    for course in catalog[studentName]:
        gradesSum, promGradesSum = sum(catalog[studentName][course]), sum([value for value in catalog[studentName][course] if value >= 5])
        stats.append((course, gradesSum / len(catalog[studentName][course]) if len(catalog[studentName][course]) > 1 and gradesSum == promGradesSum else 0))

    return stats

def getStudentStats(catalog):
    studentName = input("Introduceti numele elevului: ")
    stats = despre_elev(catalog, studentName.strip())
    for course in stats:
        print("{} {:.2f}".format(course[0], course[1]))

def adauga_nota(catalog, studentName, courseName, grades):
    if studentName in catalog and courseName in catalog[studentName]:
        catalog[studentName][courseName] += grades
    else:
        catalog[studentName] = {courseName: grades}

    return catalog

def updateStudentStats(catalog):
    studentData = input("Introduceti numele elevului, materia si notele: ").rsplit(maxsplit=3)
    studentName, courseName = studentData[:2]
    grades = [int(var) for var in studentData[2:]]

    adauga_nota(catalog, studentName.strip(), courseName.strip(), grades)
    stats = despre_elev(catalog, studentName)
    for course in stats:
        if course[0] == courseName:
            print("{} {:.2f}".format(course[0], course[1]))
            break

def main():
    catalog = getInput()
    getStudentStats(catalog)
    updateStudentStats(catalog)
    return

if __name__ == "__main__":
    main()
    exit()