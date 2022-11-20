# NoMoreHomework

# Avís: Aquest problema es impossible de resoldre. El test privat no es pot satisfer ni amb true ni amb false.

def intercalables(v1, v2):
    f = True
    for i in range(len(v1)):
        if v1[i] > v2[i]:
            f = False
    
    return f
