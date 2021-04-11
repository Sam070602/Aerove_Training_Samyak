def num_digits(n) :
    i = 0
    while True :
        n = int(n%10)
        i += 1
        if n == 0 :
            return i

def check_if_palindrome(n) :
    palindrome = 0
    m = n
    while True :
        palindrome = palindrome*10 + n%10
        n = int(n/10)
        if n == 0 :
            break
    if m == palindrome :
        return True
    
a = input("Enter number")
a = int(a)
i = a + 1

while True :
    if check_if_palindrome(i) :
        b = i
        break 
    i = i + 1

print(b)