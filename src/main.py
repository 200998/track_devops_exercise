def add(a, b, c=0):
    if type(a) != int:
        ret_a = -1
    elif a<0 or 10<a:
        ret_a = -2
    else:
        ret_a = a

    if type(b) != int:
        ret_b = -1
    elif b<0 or 10<b:
        ret_b = -2
    else:
        ret_b = b

    if type(c) != int:
        ret_c = -1
    elif c<0 or 10<c:
        ret_c = -2
    else:
        ret_c = c
    
    try:
        return int(ret_a + ret_b) + int(ret_c)
    except:
        return "error"
