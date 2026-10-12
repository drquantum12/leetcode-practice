






if __name__ == "__main__":
    MOD=10**9+1
    nums = [2,6,5,8] 
    k = 2
    bin_cnt=[0]*30
    for num in nums:
        bit=0
        while num:
            if num & 1:
                bin_cnt[bit]+=1
            num>>=1
            bit+=1

    top_k=[0]*k
    for i, count in enumerate(bin_cnt):
        val = 1<<i
        limit=min(k, count)
        for j in range(limit):
            top_k[j] |= val

    print(sum(i*i for i in top_k) % MOD)
    # print(bin_cnt)

    # ans=0
    # for _ in range(k):
    #     x=0
    #     for i in range(31):
    #         if bin_cnt[i]:
    #             x |= 1<<i
    #             bin_cnt[i]-=1
    #     print(f"{_} : {x}")
    #     ans += (x*x)
    # print(ans % MOD)
    