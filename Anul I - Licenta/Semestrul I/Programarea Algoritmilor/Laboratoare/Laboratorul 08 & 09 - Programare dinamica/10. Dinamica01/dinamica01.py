MOD = 30103
def main():
    n = int(input().strip())
    d = [[0 for _ in range(2)] for _ in range(n + 1)]
    d[0][0] = 1
    d[0][1] = 1

    for i in range(1, n + 1):
        d[i][0] = (4 * d[i - 1][1]) % MOD
        d[i][1] = (5 * d[i - 1][0]) % MOD

    answer = (d[i][0] + d[i][1]) % MOD
    print(answer)

if __name__ == "__main__":
    main()
    exit()