def main():
    n = int(input())
    
    total = 0
    
    for _ in range(n):
        a, b = map(int, input().split())
        total += (a+b) + ((b-a-1)*((a+b)/2))
        
    print(int(total))

if __name__ == "__main__":
    main()