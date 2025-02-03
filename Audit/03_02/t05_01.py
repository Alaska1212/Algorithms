def bsearch(w, h, n):
    l = 1
    r = n*max(w,h)
    while l<r:
        m = l + (r -l)//2
        count = (m // w)*(m//h)
        if count < n:
            l = m+1
        else:
            r = m
    return l

w, h, n = map(int, input().split())
print(bsearch(w, h, n))