index=0
def solve(s, index):
    res=""
    while index < len(s):
        print(f"index {index}, res={res}")
        if s[index]=="(":
            index+=1
            t, index=solve(s, index)
            res += t
        
        elif s[index]==")":
            index+=1
            return res[::-1], index
        
        else:
            res+=s[index]
            index+=1
    return res, index


if __name__ == "__main__":
    # s="(ed(et(oc))el)" => expected : "leetcode"
    s="(abcd)"
    print(solve(s,0)[0])