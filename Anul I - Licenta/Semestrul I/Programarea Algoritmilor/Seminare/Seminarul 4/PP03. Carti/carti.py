import os
path = os.path.dirname(__file__)
inputFileName = path + "/carti.csv"
outputFileName = path + "/carti.out"


def getInput():

    books = []
    with open(inputFileName, "r") as f:
        for line in f.readlines():
            title, year, price, *authors = line.split(",")
            authors = [author.replace("\"", "").strip() for author in authors]
            
            books +=  [[title, int(year), float(price), authors]]

    return books


def printBooks(books, description):
    with open(outputFileName, "a") as g:
        g.write("{}:\n\n".format(description.upper()))
        tab, outputLenMax = len(str(len(books))), 0
        for index, book in enumerate(books):
            output = "{}. Cartea <{}> scrisa de <{}> publicata in <{}> costa <{}>\n".format(
                str(index).rjust(tab),
                book[0],
                ", ".join(book[3]),
                book[1],
                book[2]
            )
            g.write(output)
            outputLenMax = max(outputLenMax, len(output))
        g.write("{}".format("-" * outputLenMax))
        g.write("\n\n")


def reducePrice(books, year, percent):
    for i in range(len(books)):
        if books[i][1] < year:
            books[i][2] = round(books[i][2] - (books[i][2] * percent) / 100, 2)

    return books


def sortBooks(books):

    def ascYear_ascTitle(item):
        return item[1], item[0]
    
    def descAutCount_descPrice(item):
        return -len(item[3]), -item[2]

    def ascFirstName_ascLastName_ascTitle_ascYear(item):
         return item[3], item[1], item[2]

    sortedBooks = sorted(books, key=ascYear_ascTitle)
    printBooks(sortedBooks, "a) Ascendent dupa an, apoi ascendent dupa titlu")

    sortedBooks = sorted(books, key=descAutCount_descPrice)
    printBooks(sortedBooks, "b) Descendent dupa numarul de autori, apoi descendent dupa pret")
    
    sortedBooks = sorted(books, key=ascFirstName_ascLastName_ascTitle_ascYear)
    printBooks(sortedBooks, "c) Ascendent dupa prenume, apoi dupa nume, apoi dupa titlu, apoi dupa an")
    
    return


def main():
    books = reducePrice(getInput(), 2000, 20)
    printBooks(books, "Cartile dupa reducerea pretului")
    
    sortBooks(books)
    return


if __name__ == "__main__":
    with open(outputFileName, "w") as g:
        next
    main()
    exit()