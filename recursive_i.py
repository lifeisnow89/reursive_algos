for i in range(0,6,1):
    print(i)

def count(rsigma):
    for i in range (rsigma,6,1):
        print(i)

def count_recursive(rsigma):
    if rsigma > 6:
        return 
    print(rsigma)
    count_recursive(rsigma)

def addup(rsigma):
    if rsigma < 1:
        return 0
    return rsigma + addup(rsigma-1)

print(addup(5))
print(addup(round(2.5)))
print(addup(-1))

def rfact(rsigma):
    if rsigma < 2:
        return 1
    return rsigma * rfact(rsigma-1)

print(rfact(3))
print(rfact(round(6.5)))