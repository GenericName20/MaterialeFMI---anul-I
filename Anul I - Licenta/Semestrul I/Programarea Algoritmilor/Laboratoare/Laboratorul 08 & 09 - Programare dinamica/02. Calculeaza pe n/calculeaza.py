# 60 de puncte - Ineficient in Python, vezi sursa C++
# Starea: d[i] - Numarul minim de operatii necesare pentru a ajunge la numarul i
# Starea initiala: d[1] = 0 - Numarul 1 este la baza celorlalte operatii, nu poate fi calculat
# Relatia de recurenta: d[i] = 1 + min(d[i - 1], d[i / 2], d[i / 3])

def main():
    n = int(input())
    d = [0] * (n + 1)
    # d[1] = 0
    for i in range(2, n + 1):
        d[i] = 1 + min(d[i - 1], 
                       d[i // 2] if (i % 2 == 0) else d[i - 1],
                       d[i // 3] if (i % 3 == 0) else d[i - 1])

    print(d[n])

if __name__ == "__main__":
    main()
    exit()