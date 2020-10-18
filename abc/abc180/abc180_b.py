import math

def main():
    n = int(input())
    x = list(map(int, input().split()))
    print(sum(list(map(abs, x))))
    print(math.sqrt(sum(map(lambda i: math.pow(i, 2), map(abs, x)))))
    print(max(list(map(abs, x))))

if __name__ == "__main__":
    main()