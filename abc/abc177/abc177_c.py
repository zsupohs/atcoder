from random import randint

def main():
    n = int(input())
    a = list(map(int, input().split()))
    # a = [randint(1, 10**9) for i in range(n)]
    print(abc177_c(n, a))

def abc177_c(n, a):
    ans = 0
    
    # for i in range(n):
    #     for j in range(i+1, n):
    #         ans += a[i]*a[j]
    #         ans %= (10**9+7)
    
    total = a[n-1]    
    for i in reversed(range(n-1)):
        ans += a[i] * total
        ans %= (10**9+7)
        total += a[i]
    
    return ans

if __name__ == "__main__":
    main()
    