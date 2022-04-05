print("PTUK", end="")
x = 10
x = x + 5
print(type(x))

x = 10
y = 4
print(x / y)  # 2.5
print(x // y)  # 2

x = -10
y = 4
print(x//y)  # -3 why?  bcoz -12 / 4 = -3
print(x % y)  # 2


if x > 7:
    print("yes")
    print("yes")
else:
    print("no")


for x in [1, 2, 3, 4]:
    print(x)

for x in range(5):
    print(x)
# range(start, stop, step)
for x in range(0, 5, 1):
    print(x)

# ========================
for x in "PTUK":
    print(X)
else:
    print("XYZ")
# ========================

for x in [1, "A", 2, 'B']:
    print(type(x))
else:
    print("XYZ")


# prime number


x = int(input())  # receive input and convert it to int
x = x + 1
print(x)
print(bin(x))
print(oct(x))
print(hex(x))


def fun(x, y):
    if(x > y):
        print("PTUK")
        return x
    return y


print(fun(10, 20))
f = fun
f()
