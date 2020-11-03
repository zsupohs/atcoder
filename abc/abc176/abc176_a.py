from math import ceil

def main():
    n, x, t = map(int, input().split())
    print(ceil(n/x)*t)

if __name__ == "__main__":
    main()