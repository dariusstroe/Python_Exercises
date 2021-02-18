
isMale=True
isTall=False

if isMale and isTall:
    print("You are a male and tall")
elif isMale and not(isTall):
    print("You are a short male")
elif isTall and not(isMale):
    print("You are tall but not male")
else:
    print("You are neither male nor tall")

def MaxNumber(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num1<=num2 and num1>=num3:
        return num2
    elif num1<=num2 and num2<=num3:
        return num3

print(MaxNumber(1,7,23))