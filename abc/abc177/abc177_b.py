def main():
    s = input()
    t = input()
    ls = len(s)
    lt = len(t)
    
    ans = 1000
    
    for i in range(ls):
        cnt = 0
        if len(s[i:i+lt]) < lt:
            break
        for j, k in zip(s[i:i+lt], t):
            if j != k:
                cnt += 1
        
        ans = min(ans, cnt)
    
    print(ans)
    
if __name__ == "__main__":
    main()