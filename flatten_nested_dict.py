def flatten(d_):
    res=dict()
    def dfs(k,d):
        if isinstance(d, dict):
            for i in d:
                dfs(k+"."+i, d[i])
        else:
            res[k]=d
    for i in d_:
        dfs(i,d_[i])
    return res
        
        




if __name__ == "__main__":
    d_= {'a':5, 'b':{'c':6, 'd':7}, 'e':8, 'f':{'g':{'h':9}}, 'i':{'j':4, 'k':{'l':3,'n':5, 'm':{}}}}
    print(flatten(d_))