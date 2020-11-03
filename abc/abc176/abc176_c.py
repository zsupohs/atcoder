def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0 for _ in range(n)]
    
    for i in range(1, n):
        if a[i] < a[i-1] + b[i-1]:
            b[i] = a[i-1] + b[i-1] - a[i]
    
    print(sum(b))
    
if __name__ == "__main__":
    main()