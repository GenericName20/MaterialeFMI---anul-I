# Pentru editorul de text
# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/cinema.in"

inputFileName = "cinema.in"

def getInput():
    cinemas = {}
    with open(inputFileName, "r") as f:
        for line in f.readlines():
            cinemaName, filmName, hours = line.split("%")
            cinemaName = cinemaName.strip()
            filmName = filmName.strip()
            hours = [hour for hour in hours.split()]

            if cinemaName not in cinemas:
                cinemas[cinemaName] = {filmName: hours}
            else:
                cinemas[cinemaName][filmName] = hours

    return cinemas

def delFilm(cinemas):
    def sterge_ore(cinemas, cinemaName, filmName, hours):
        try:
            for hour in cinemas[cinemaName][filmName]:
                if hour == hours:
                    cinemas[cinemaName][filmName].remove(hour)
                    if cinemas[cinemaName][filmName] == []:
                        del cinemas[cinemaName][filmName]
                if len(cinemas[cinemaName]) == 0:
                    del cinemas[cinemaName]
                    return "Nu mai exista filme in {}".format(cinemaName)
            return [film for film in cinemas[cinemaName]]
        except:
            return "Input invalid!"
        
    f, c, o = input("Numele filmului: ").strip(), input("Cinematograful: ").strip(), input("Ora: ").strip()
    films = sterge_ore(cinemas, c, f, o)
    return films

def cinema_film(cinemas, minHour, maxHour, *cinemaNames):
    def sortKey(item):
        return item[0], -len(item[2])
    
    ans = []
    for name in cinemaNames:
        for film in cinemas[name]:
            cond = False
            for hour in cinemas[name][film]:
                if hour >= minHour and hour <= maxHour:
                    cond = True
                    break
            if cond:
                ans.append((film, name, cinemas[name][film]))
    
    return sorted(ans, key=sortKey)

def writeOutput(cinemas, answer):
    print("Cerinta 1: {}\n{}\nCerinta 2: {}".format(answer[0], cinemas, answer[1]))
    return

def main():
    cinemas = getInput()
    answer = delFilm(cinemas), cinema_film(cinemas, "14:00", "22:00", "Cinema 1", "Cinema 2")
    writeOutput(cinemas, answer)
    return

if __name__ == "__main__":
    main()
    exit()