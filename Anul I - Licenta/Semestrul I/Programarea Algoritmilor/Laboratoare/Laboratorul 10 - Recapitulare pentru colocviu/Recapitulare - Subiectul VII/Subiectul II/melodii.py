# Minciunescu Vlad-Andrei - 151

# import os
# path = os.path.dirname(__file__)
# inputFileName = path + "/melodii.in"
# outputFileName = path + "/melodii.out"

inputFileName = "melodii.in"
outputFileName = "melodii.out"

def citire_date():
    songs = {}
    with open(inputFileName, "r") as f:
        for line in f.readlines():
            if line.strip().startswith("Gen"):
                gbg, genre = line.split(">>", maxsplit=2)
                genre = genre.strip()
                songs[genre] = {}
            else:
                name, artist, duration = [word.strip() for word in line.rsplit("/", maxsplit=2)]
                songs[genre][name] = (artist, duration)
   
    return songs

def playlist(songs, *genres, durata_minima="02:00", durata_maxima="03:30"):
    choices = []
    for genre in genres:
        try:
            for song in songs[genre]:
                if songs[genre][song][1] >= durata_minima and songs[genre][song][1] <= durata_maxima:
                    choices.append((genre, song, songs[genre][song][0], songs[genre][song][1]))
        except:
            next
    
    choices = sorted(choices, key=lambda item: (item[3][::-1], item[2], item[1]))
    return choices

def adauga_melodie(songs, genre, title, artist, durata):
    try:
        songs[genre][title] = (artist, durata)
        print("Genul {} contine acum {} melodii.".format(genre, len(songs[genre])))
    except:
        print("Nu exista acest gen muzical!")

def main():
    # Subtask A
    songs = citire_date()
    
    # Subtask B
    task_b = playlist(songs, "Rock", "Hip-hop")
    for line in task_b:
        print(line)

    # Subtask C
    gen, titlu, artist, durata = input("Gen: ").strip(), input("Titlu: ").strip(), input("Artist: ").strip(), input("Durata: ").strip()
    adauga_melodie(songs, gen, titlu, artist, durata)

if __name__ == "__main__":
    main()
    exit(0)