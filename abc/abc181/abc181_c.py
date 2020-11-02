from collections import Counter

def main():
    n = int(input())
    p = [tuple(map(int, input().split())) for _ in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1 = p[i]
                x2, y2 = p[j]
                x3, y3 = p[k]
                dx1 = x2 - x1
                dy1 = y2 - y1
                dx2 = x3 - x1
                dy2 = y3 - y1
                if dx1 * dy2 == dx2 * dy1:
                    print("Yes")
                    exit()
    
    print("No")

if __name__ == "__main__":
    main()