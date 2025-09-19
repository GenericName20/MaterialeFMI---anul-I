# Abordarea solutiei se incadreaza in tehnica Backtracking, deoarece:
# Pentru fiecare solutie generata, ne bazam pe o conditie externa:
# Fiecare x[k] | 0 <= k < n, preia valori din multimea A = {1, 2, 3, ..., n}

# De asemenea, solutiile sunt validate de conditia interna:
# Fiecare x[k] | 0 <= k < n trebuie sa fie unic intr-o solutie generata, deci diferit de orice x[i], i < k

# Conditia de existenta a solutiei presupune ca lungimea unei solutii sa aiba lungimea
# specificata in enunt

# In plus, se incearca generarea a cat mai multe solutii corecte
# fiind fortata verificarea tuturor posibilitatilor

x, n = [], 0
def afisare_solutie(k):
    # print(*x), dar trebuie sa fie vizibil ca s-a ales o solutie de lungime k
    for i in range(k + 1):
        print(x[i], end="")
    print()

def cond(k):
    # verificam daca elementul ales pentru pozitia x[k] exista deja in solutie
    for i in range(k):
        if x[i] == x[k]:
            return False
    return True

def sol(k):
    return k == n - 1

def bt(k):
    global x
    for i in range(1, n + 1):
        x[k] = i
        if (cond(k)):
            if (sol(k)):
                afisare_solutie(k)
            else:
                bt(k + 1)

def main():
    global n, x
    n = int(input())
    x = [0] * n
    bt(0)

if __name__ == "__main__":
    main()
    exit(0)