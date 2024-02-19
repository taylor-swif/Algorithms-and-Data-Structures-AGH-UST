from zad2testy import runtests


def merg(L, P):
    i = 0
    j = 0
    l = len(L)
    p = len(P)
    Merged = []
    #print(L, P)
    while i < l and j < p:
        if L[i][0] < P[j][0]:
            Merged.append(L[i])
            i += 1
        elif L[i][0] == P[j][0]:
            if L[i][1] > P[j][1]:
                Merged.append(L[i])
                i += 1
            else:
                Merged.append(P[j])
                j += 1
        else:
            Merged.append(P[j])
            j += 1

    while i<l:
        Merged.append(L[i])
        i += 1
    while j<p:
        Merged.append(P[j])
        j += 1

    return Merged


def mergsort(A, p, k):
    #print("Rekursja")
    if p == k:
        #print("najmniejsza")
        return [A[p]]
    else:
        #print("glebiej ",p,k)
        L = mergsort(A, p,(p+k) // 2)
        P = mergsort(A, ((p+k) // 2) + 1, k)

        New = merg(L, P)
        #print(New," Nowa")

        return New


def depth(L):
    # tu prosze wpisac wlasna implementacje
    A = []
    for i in L:
        A.append([i[0], i[1], 1])

    #A = sorted(A, key=lambda x: x[1],reverse=True)
    #A=sorted(A, key=lambda x:x[0])
    A = mergsort(A, 0, len(A) - 1)

    Bucket = []
    for i in A:
        flag = True
        for j in Bucket:
            if j[0] <= i[0] and j[1] >= i[1]:
                j[2] += i[2]
                flag = False

            elif j[0] >= i[0] and j[1] <= i[1]:
                j[0] = i[0]
                j[1] = i[1]
                j[2] += i[2]
                flag = False

        if flag:
            Bucket.append(i)

    maks = 0
    print(Bucket, "dlugosc", len(Bucket))
    for i in Bucket:
        if i[2] > maks:
            maks = i[2]

    maks -= 1

    print(len(Bucket), len(L))

    return maks


runtests(depth)