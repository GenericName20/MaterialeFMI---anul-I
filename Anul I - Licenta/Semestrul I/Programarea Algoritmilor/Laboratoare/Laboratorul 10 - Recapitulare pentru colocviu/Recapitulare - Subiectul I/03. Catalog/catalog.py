# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/catalog.in"

inputFileName = "catalog.in"

def getInput():
    catalog = {}
    with open(inputFileName, "r") as f:
        studentsNumber = int(f.readline().strip())
        for _ in range(studentsNumber):
            *studentName, gradesNumber = f.readline().split()
            studentName = " ".join(studentName)
            catalog[studentName] = {}

            for _ in range(int(gradesNumber)):
                course, *grades = f.readline().split(",")
                grades = [int(grade) for grade in grades]
                if course not in catalog[studentName]:
                    catalog[studentName][course] = grades
                else:
                    catalog[studentName][course] += grades

    return catalog

def detalii_elev(catalog, studentName):
    stats = []
    for course in catalog[studentName]:
        average = sum(catalog[studentName][course]) / len(catalog[studentName][course]) if len(catalog[studentName][course]) > 1 else 0
        if average >= 5:
            stats.append((course, average))
        else:
            stats.append((course, 0))
    
    return sorted(stats)

def showStudentStats(catalog):
    studentName = input("Numele elevului: ").strip()
    
    stats = detalii_elev(catalog, studentName) if studentName in catalog else []

    for stat in stats:
        print("{} {:.2f}".format(stat[0], stat[1]))   

    return

def showStudentRanking(catalog):
    def computeRanking(catalog, *studentNames):
        studentsRanking = []
        for student in studentNames:
            studentStats, average = detalii_elev(catalog, student), 0
            for course in range(len(studentStats)):
                if studentStats[course][1] == 0:
                    average = 0
                    break
                else:
                    average += studentStats[course][1]
            
            studentsRanking.append((student, average / (course + 1) if average != 0 else 0))

        return sorted(studentsRanking, key=lambda item: -item[1])

    studentsRanking = computeRanking(catalog, "Alin Enache", "Ioana Matei")
    
    for pair in studentsRanking:
        print("{}: {}".format(pair[0], pair[1]))
    
    return

def main():
    catalog = getInput()
    showStudentStats(catalog)
    showStudentRanking(catalog)
    return

if __name__ == "__main__":
    main()
    exit()