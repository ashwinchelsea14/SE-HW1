def swap(a,b):
    t = a
    a = b
    b = t
    return a,b

# q = 10
# w = 20
q,w = 10,20
q,w = swap(q,w)
print (q,w[:])
#simply we can,
# q,w = w,q
# print(q,w)