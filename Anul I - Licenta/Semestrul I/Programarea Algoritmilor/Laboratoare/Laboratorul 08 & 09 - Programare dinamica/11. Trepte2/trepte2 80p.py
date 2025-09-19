MOD = 9001
def main():
    n, k = map(int, input().strip().split())
    d = [0] + [1] + [0] * (n - 1)

    for i in range(2, n + 1):
        for j in range(1, k + 1):
            d[i] += d[i - j] % MOD
        d[i] %= MOD

    print(d[n] % MOD)
    return

if __name__ == "__main__":
    main()
    exit()