MOD = 9001
def main():
    n, k = map(int, input().strip().split())
    d = [0] + [1] + [0] * (n - 1)
    last = 1

    for i in range(2, n + 1):
        d[i] = last % MOD
        if (i - k >= 0):
            last -= d[i - k] % MOD
        last += d[i]
        
    print(d[n] % MOD)
    return

if __name__ == "__main__":
    main()
    exit()