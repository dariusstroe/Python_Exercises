def Power(base,power):
    for i in range(int(power/2)):
        base*=base
    return base

print(Power(3,2))


def RaiseToPower(baseNumber,powerNumber):
    result=1
    for index in range(powerNumber):
        result=result*baseNumber
    return result

print (RaiseToPower(3,4))