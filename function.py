def makeList(f):
    f2 = []
    current = 0
    for i in f:
        if i.isdigit():
            i = int(i)
            print(i)
            if current == 0:
                current = i
            else:
                current = (current * 10) + i
        else:
            if current != 0:
                f2.append(current)
                current = 0
            f2.append(i)
    if current != 0:
                f2.append(current)
                current = 0
    return f2


def functionDoer(f, x):
    arithmatic = "+-*/"
    for i in range(len(f)):
        if f[i] == "x":
            print("w")
        if f[i] == "*":
            f[i] = int(f[i - 1]) * int(f[i + 1])
            f2 = f
            del f2[i - 1]
            del f2[i]
            return(functionDoer(f2, x))

        elif f[i] == "/":
            f[i] = int(f[i - 1]) / int(f[i + 1])
            f2 = f
            del f2[i - 1]
            del f2[i]
            return(functionDoer(f2, x))

    return f


f = input()
f = makeList(f)
print(f)
#x = i nput()
#f = list(f)
# f = functionDoer(f, x)  print(float(f[0]))  print(f)