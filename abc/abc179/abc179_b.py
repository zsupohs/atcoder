def main():
    n = int(input())
    d = [input().split() for _ in range(n)]
    count = 0
    for x in d:
        count = count + 1 if x[0] == x[1] else 0
        if count >= 3:
            print('Yes')
            exit()
    print('No')

if __name__ == "__main__":
    main()