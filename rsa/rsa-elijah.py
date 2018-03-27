# parrallel arrays
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numerical_eqivalent = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14",
                       "15","16","17","18","19","20","21","22","23","24","25"]

# Converts a number from base 10 to base 2, returns a string 
def convertb10tob2(n):
    if(n == 0):
        return  ''
    else:
        return convertb10tob2(n//2) + str(n%2)

# b^a mod n
def bToAModN(b, a, n):

    print("let x = 1")
    x = 1
    power = b % n
    print("Let power = {} % {} = {} ".format(b, n, power))
    for i in range(0,len(a)):
        if a[i] == '1':
            x = (x*power) % n
            print("x*power % n =" + str(x))
        power = (power * power) % n
        print("power * power % n " + str(power))

    return x
            
# Test bToAModN() function
def test_bToAModN():
    a = convertb10tob2(676)
    # String has to be reverseed
    x =bToAModN(2, a[::-1], 645)
    print(x) # 16 

def get_alphabetic_equivalent(a):

    if len(a) == 3:
        a = "0" + a # append a zero for the first character because the representations are pairs like 01 

    m_split = [a[i:i+2] for i in range(0, len(a), 2)] # "HELP" => ["HE", "LP"]

    first_double = m_split[0]
    second_double = m_split[1]

    # Special cases 
    if len(first_double) == 1:
        first_double = "0" + first_double

    if len(second_double) == 1:
        second_double = "0" + second_double

    # Return the string representation 
    d1 = str(alphabet[numerical_eqivalent.index(first_double)])
    d2 = str(alphabet[numerical_eqivalent.index(second_double)])
    return d1+d2

def get_numerical_equivalent(a):
    # Get the pairs 
    first_char = a[0]
    second_char = a[1]
    # Return the numericcal representation 
    n1 = str(numerical_eqivalent[alphabet.index(first_char)])
    n2 = str(numerical_eqivalent[alphabet.index(second_char)])
    return int((n1 + n2))

def encrypt(n, e, m):

    # split the string up by two characters
    m_split = [m[i:i+2] for i in range(0, len(m), 2)] # "HELP" => ["HE", "LP"]

    # convert to numbers
    nums = [get_numerical_equivalent(m_split[i]) for i in range(0, len(m_split))]
    print("Encoded numbers: " + str(nums))

    # Encrypt the numbers using bToAModN
    C = [bToAModN(nums[i], convertb10tob2(e)[::-1], n) for i in range(0, len(nums))]
    return C
        
def decrypt(n, c, d):
    M = [] # Message
    for i in range(0, len(c)):
        m = bToAModN(c[i], convertb10tob2(d)[::-1], n) # decrypt each number 
        M.append(m) # append it to the array 
    print("Decrypted numbers " + str(M))

    # convert the decrypted number into strings 
    message = [get_alphabetic_equivalent(str(M[i])) for i in range(0, len(M))]
    return ''.join(message) # pack it into a single string and return it 

def main():
    e = 17 # encryption 
    d = 2753 # decryption 
    n = 4819 # base 

    # A) Encrypt the message HELP by breaking into the two blocks "HE" and "LP" and encrypting each block
    m = "HELP"
    print("Input message :" + str(m))
    C = encrypt(n, d, m)
    print("Encrypted numbers " + str(C))
    M =decrypt(n,C,e)
    print("Output message: " + M)

    # B) Decrypt the message where each integer corresponds to two letters 
    encrypted_message = [3797, 516, 2296, 3865, 1689]
    decrypted_message = decrypt(n, encrypted_message, e)

main()
