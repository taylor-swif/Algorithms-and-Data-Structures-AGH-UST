from zad2testy import runtests

def mergesort(T):
    if len(T) == 1:
        return T
    n = len(T)
    ans1 = mergesort(T[:n//2])
    ans2 = mergesort(T[n//2:])
    len1 = len(ans1)
    len2 = len(ans2)
    i = j = 0

    ans = []
    while i < len1 and j < len2:
        if ans1[i][0] < ans2[j][0]:
            ans.append(ans1[i])
            i += 1
        else:
            ans.append(ans2[j])
            j += 1

    while i < len1:
        ans.append(ans1[i])
        i += 1
    while j < len2:
        ans.append(ans2[j])
        j += 1

    return ans

def depth(L):
    
    beg = [[L[i][0], i] for i in range(len(L))]
    end = [[L[i][1], i] for i in range(len(L))]
    #for i in range(len(L)):
    #    a, b = L[i]
    #    beg.append([a, i])
    #    end.append([b, i])

    beg = mergesort(beg)
    end = mergesort(end)
    print(beg)
    print(end)
    f = [-1 for i in range(len(L))]
    g = [-1 for i in range(len(L))]
    i = 0
    while i < len(L):
        ix1 = beg[i][1]
        f[ix1] = i
        print(f)
        ix = i
        while i < len(L)-1 and beg[i+1][0] == beg[i][0]:
            f[beg[i+1][1]] = ix
            print(f)
            i += 1
        i += 1
    i = len(L)-1
    res = -1
    while i >= 0:
        ix2 = end[i][1]
        g[ix2] = i
        print(g)
        ix = i
        res = max(res, g[i]-f[i])
        while i-1 >= 0 and end[i-1][0] == end[i][0]:
            g[end[i-1][1]] = ix
            i -= 1
            print(g)
            res = max(res, g[i]-f[i])
        i -= 1
    print(f, g)
    
        
    return res
print(depth([[1, 6], [5, 6], [2, 5], [8, 9], [1, 6]]))
#runtests( depth ) 
