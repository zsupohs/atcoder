def main():
    n = int(input())
    print(sum((n-1) // i for i in range(1, n+1)))
    
if __name__ == "__main__":
    main()
