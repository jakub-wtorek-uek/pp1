def isAdult(age):
    if age < 18:
        return False

    return True


paul_age = 21
annie_age = 18

if isAdult(paul_age) and isAdult(annie_age):
    print("Both are adults")
