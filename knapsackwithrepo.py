weightsofitems = [2,7,9,3]
valueofitems = [8,2,6,30] 

W = 10
i = 1
K = [0] #K(0) = 0

while i <= W:
    w = weightsofitems[i]
    vi = valueofitems[i]
    Ki = weightsofitems[i]-1
    K.append(0)
    if w <= i:
        K[i] = max(K[Ki] + vi)
        print(K[i])
    i = i+1
    print(K[0])
    