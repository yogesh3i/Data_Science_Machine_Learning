a=10
def fun():
    global a
    a=15
    print("inside function",a)

fun()
print("Outside the function",a)
print(a)