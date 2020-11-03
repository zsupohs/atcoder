def main():
    n = input()
    print("Yes" if sum(map(int, n.split())) % 9 == 0 else "No")

if __name__ == "__main__":
    main()