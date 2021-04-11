f = open("myFirstFile.txt", "w")
def check_if_prime(n) :
    if n == 1 :
        return False
    for i in range(2, int(n/2) + 1) :
        if n%i == 0 :
            return False
    return True

def num_digits(n) :
    i = 0
    while True :
        n = int(n%10)
        i += 1
        if n == 0 :
            return i

def check_twin_primes(n) :
    if(check_if_prime(n) and check_if_prime(n + 2)) :
        return True
    return False

a = input("Enter number of digits")
a = int(a)
b = 10**(a-1)
for i in range(b, (10**a) - 2) :
    if check_twin_primes(i) :
        f.write(str(i) +" "+str(i+2)+"\n")

f.close()