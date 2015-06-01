num = 10

def PrimeNumber(num):

    prime = "true"

    for i in range(2,num)[::-1]:
        if num% i == 0:
            prime = "false"
    return prime

print PrimeNumber(num)
