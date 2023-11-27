def makeList(f):
    f2 = []
    current = 0
    for i in f:
        if i.isdigit():
            i = int(i)
            if current == 0:
                current = i
            else:
                current = (current * 10) + i
        else:
            if current != 0:
                f2.append(current)
                current = 0
            if i != " ":
                f2.append(i)
    if current != 0:
                f2.append(current)
                current = 0
    return f2

def findx(f,x):
    for i in range(len(f)):
        if f[i] == "x" and i > 0:
            if isinstance(f[i-1],int):
                f[i - 1] = x * f[i-1]
                del f[i]
                return(findx(f,x))
        elif f[i] == "x":
            f[i] = x
    return f


def functionDoer(f, x):
    
    f = power(f,x)
    f = xAndDiv(f,x)
    f = addAndSub(f,x)
    return f

def power(f,x):
    for i in range(len(f)):
        if f[i] == "^":
            new = list
            new = f[:i - 1]
            new.append(f[i - 1] ** f[i + 1])
            new = new + f[(i + 2):]
            return xAndDiv(new, x)
    return f

def xAndDiv(f,x):
    for i in range(len(f)):
        if f[i] == "*":
            new = list
            new = f[:i - 1]
            new.append(f[i - 1] * f[i + 1])
            new = new + f[(i + 2):]
            return xAndDiv(new, x)
        elif f[i] == "/":
            new = list
            new = f[:i - 1]
            new.append(f[i - 1] / f[i + 1])
            new = new + f[(i + 2):]
            return xAndDiv(new, x)
    return f

def addAndSub(f,x):
    for i in range(len(f)):
        if f[i] == "+":
            new = list
            new = f[:i - 1]
            new.append(f[i - 1] + f[i + 1])
            new = new + f[(i + 2):]
            return addAndSub(new, x)
        elif f[i] == "-":
            new = list
            new = f[:i - 1]
            new.append(f[i - 1] - f[i + 1])
            new = new + f[(i + 2):]
            return addAndSub(new, x)
    return f 


f = input()
x = int(input())
f = makeList(f)
f = findx(f,x)
f = functionDoer(f, x)  
print(f[0])
