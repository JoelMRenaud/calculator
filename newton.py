from function import funct

f = input("Input function ")
dx = input("Input derivative of the function ")
xn = 1

guess = 2
while((int(xn * 100000)) / 100000.0 != (int(guess * 100000)) / 100000.0):
    guess = xn
    xn = xn - (funct(f, xn) / funct(dx, xn))

print(xn)