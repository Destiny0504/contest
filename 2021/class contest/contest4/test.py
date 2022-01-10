def lcs(X, Y, m, n):
    # m,n為X,Y字串的長度
    # 若m或n為0, 代表沒有lcs
    if(m == 0 or n == 0):
        return 0
    #比較X[m-1]與Y[n-1], 字串中最後一個字元
    #若相等, 則代表只需比較最後一個之前的字串, 再加一(最後一個字元)即可
    elif(X[m-1] == Y[n-1]):
        return lcs(X, Y, m-1, n-1) + 1
    #若不相等, 就不必比較最後一個字元
    else:
        return max(lcs(X, Y, m, n-1), lcs(X, Y, m-1, n))