import os
path = os.path.dirname(__file__)
inputFileName = path + "/studenti.csv"
outputFileName = path + "/studenti.out"

def getInput():
    students = []

    with open(inputFileName, "r") as f:
        for line in f.readlines():
            lastName, group, *grades = line.strip().split(",")
            
            grades = [int(grade) for grade in grades if grade != ""]
            
            students.append(tuple([lastName, int(group.strip()), grades]))

    return students


def writeStudents(students, description):
    with open(outputFileName, "a") as g:
        g.write("{}:\n\n".format(description.upper()))
        for index, student in enumerate(students):
            g.write("{}. Elevul <{}> din grupa <{}> cu mediile <{}> este {}\n".format(
                str(index + 1).rjust(len(str(len(students)))),
                student[0].upper(),
                student[1],
                 ", ".join([str(grade) for grade in student[2]]),
                "PROMOVAT" if student[3] else "NEPROMOVAT"))
            
        g.write("{}\n\n".format("-" * 100))

def promovate(students):
    minimumCC = int(input("Puncte credit necesare: "))

    for index, student in enumerate(students):
        totalCC = 0
        for grade in student[2]:
            if grade == 0:
                totalCC = 0
                break
            else:
                totalCC += 5 * grade

        students[index] += tuple([True]) if totalCC >= minimumCC else tuple([False])

    return students

def sortStudents(students):
    def ascGroup_ascAlpha(item):
        return item[1], item[0]

    def ascProm_ascAlpha(item):
        return -item[3], item[0]

    def descSumCC_ascGroup_ascAlpha(item):
        return -sum(item[2]), item[1], item[0]

    def ascGroup_ascProm_ascSumCC_ascAlpha(item):
        return item[1], -item[3], -sum(item[2]), item[0]
    
    sortedStudents = sorted(students, key=ascGroup_ascAlpha)
    writeStudents(sortedStudents, "a) Ascendent dupa grupa, iar fiecare elev al grupei in ordine lexicografica")

    sortedStudents = sorted(students, key=ascProm_ascAlpha)
    writeStudents(sortedStudents, "b) Ascendent dupa promovabilitate, iar fiecare elev promovat, apoi nepromovat, in ordine lexicografica")

    sortedStudents = sorted(students, key=descSumCC_ascGroup_ascAlpha)
    writeStudents(sortedStudents, "c) Descendent dupa suma creditelor, apoi dupa grupa, apoi in ordine lexicografica")

    sortedStudents = sorted(students, key=ascGroup_ascProm_ascSumCC_ascAlpha)
    writeStudents(sortedStudents, "d) Ascendent dupa grupa, apoi dupa promovabilitate, apoi dupa suma creditelor, apoi in ordine lexicografica")

    return

def main():

    with open(outputFileName, "w"):
        next

    students = getInput()
    students = promovate(students)
    sortStudents(students)
    return


if __name__ == "__main__":
    main()
    print("Output written in {}\n".format(outputFileName))
    exit()