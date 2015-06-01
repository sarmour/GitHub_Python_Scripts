def FirstFactorial(num):
    print num
    val = int(num)

    for i in range(1, val):
        val *= i
    return val

print FirstFactorial(5)
