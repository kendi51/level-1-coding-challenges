def has_three(num1 = 5, num2 = 7):
    sum = num1 + num2
    three = "3"
    if three in str(num1):
        return True
    if three in str(num2):
        return True
    if three in str(sum):
        return True
    
    return False

has_three()