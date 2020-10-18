from math import sqrt, ceil

def main():
    n = int(input())
    ans = []
    for i in range(1, ceil(sqrt(n))+1):
        if n % i == 0:
            ans.append(i)
            ans.append(n // i)

    for i in sorted(list(set(ans))):
        print(i)

if __name__ == "__main__":
    main()