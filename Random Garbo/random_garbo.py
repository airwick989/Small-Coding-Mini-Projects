def isPrime(num):
    num = abs(num)
    if num < 2:
        return False
    for i in range(2, num):
        if (num / i).is_integer():
            return False
    
    return True

for i in range(-100, 100):
    if isPrime(i):
        print(i)