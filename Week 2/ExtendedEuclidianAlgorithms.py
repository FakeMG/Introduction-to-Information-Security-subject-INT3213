def extended_euclidian(a, b):
    if b == 0:
        d,x,y = a,1,0
        return [d,x,y]
    # a*0 + b*1 = b
    x1 = 0
    y1 = 1

    # a*1 + b*0 = a
    x2 = 1
    y2 = 0
    
    while b > 0:
        q = a // b
        r = a % b

        # a*x + b*y = r
        x = x2 - q * x1
        y = y2 - q * y1

        a = b
        b = r
        x2 = x1
        x1 = x
        y2 = y1
        y1 = y
    
    d = a
    x = x2
    y = y2
   
    return [d,x,y]
    
    
a = 25
b = 22

print(extended_euclidian(a,b)) 