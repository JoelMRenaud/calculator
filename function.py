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
            else:
                f[i] = x
        elif f[i] == "x":
            f[i] = x
    return f


def functionDoer(f, x):
    new = []
    bracket = 0
    for i in range(len(f)):
        if f[i] == ")":
            bracket = bracket - 1
        elif f[i] == "(":
            new = new + functionDoer(f[i + 1:],x)
            bracket = bracket + 1
            if i > 0:
                if isinstance(f[i-1],int):
                    newVal = new[len(new) - 1] * new[len(new) - 2]
                    new.pop()
                    new.pop()
                    new.append(newVal)
        elif bracket == 0:
            test = [f[i]]
            new = new + test
        
    f = new    
    f = power(f,x)
    f = xAndDiv(f,x)
    f = addAndSub(f,x)
    return f

def power(f,x):
    for i in range(len(f)):
        if f[i] == "^":
            new = []
            new = f[:i - 1]
            new.append(f[i - 1] ** f[i + 1])
            new = new + f[(i + 2):]
            return power(new, x)
    return f

def xAndDiv(f,x):
    for i in range(len(f)):
        if f[i] == "*":
            new = []
            new = f[:i - 1]
            new.append(f[i - 1] * f[i + 1])
            new = new + f[(i + 2):]
            return xAndDiv(new, x)
        elif f[i] == "/":
            new = []
            new = f[:i - 1]
            new.append(f[i - 1] / f[i + 1])
            new = new + f[(i + 2):]
            return xAndDiv(new, x)
    return f

def addAndSub(f,x):
    for i in range(len(f)):
        if f[i] == "+":
            new = []
            new = f[:i - 1]
            new.append(f[i - 1] + f[i + 1])
            new = new + f[(i + 2):]
            return addAndSub(new, x)
        elif f[i] == "-":
            new = []
            new = f[:i - 1]
            new.append(f[i - 1] - f[i + 1])
            new = new + f[(i + 2):]
            return addAndSub(new, x)
    return f 

def funct(f,x):
    f = makeList(f)
    f = findx(f,x)
    f = functionDoer(f, x)  
    return f[0]
