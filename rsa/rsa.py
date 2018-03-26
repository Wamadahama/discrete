# parrallel arrays
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numerical_eqivalent = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,
                       15,16,17,18,19,20,21,22,23,24,25]

def convertb10tob2(n):
    if(n == 0):
        return  ''
    else:
        return convertb10tob2(n//2) + str(n%2)

def bToAModN(b, a, n):

    x = 1
    power = b % n

    #print(len(a))
    #print("power init: " + str(power))

    for i in range(len(a)):
        if a[i] == '1':
            x = (x*power) % n
        #    print("x: " + str(x))
        power = (power * power) % n
        #print("power: " + str(power))

    return x
            

def test_bToAModN():
    a = convertb10tob2(676)
    # String has to be reverseed
    x =bToAModN(2, a[::-1], 645)
    print(x) # 16 

def get_numerical_equivalent(a):
    first_char = a[0]
    second_char = a[1]
    n1 = str(numerical_eqivalent[alphabet.index(first_char)])
    n2 = str(numerical_eqivalent[alphabet.index(second_char)])
    return int((n1 + n2))

def get_alphabetic_equivalent(a):
    first_double = a[0]
    second_double = a[1]
    d1 = str(alphabet[numerical_eqivalent.index(first_double)])
    d2 = str(alphabet[numerical_eqivalent.index(second_double)])
    return d1+d2

def encrypt(n, e, m):
    # split the string up by two characters
    m_split = [m[i:i+2] for i in range(0, len(m), 2)] # "HELP" => ["HE", "LP"]
    # convert to numbers
    nums = [get_numerical_equivalent(m_split[i]) for i in range(0, len(m_split))]
    print(nums)

    binary_nums = []
    for i in range(0, len(nums)):
        binary_nums.append(str(convertb10tob2(nums[i])))

    C = [bToAModN(e,binary_nums[i][::-1],n) for i in range(0, len(binary_nums))]
    return C
        
def decrypt(n, c, d):
    binary_nums = [convertb10tob2(c[i]) for i in range(0, len(c))]
    M = [bToAModN(d,binary_nums[i][::-1], n) for i in range(0, len(binary_nums))]
    print(M)

def main():
    e = 17 # encryption 
    d = 2753 # decryption 
    n = 4819 

    #print(get_numerical_equivalent("HE"))
    #print(get_numerical_equivalent("LP"))
    m = "HELP"
    C = encrypt(n, e, m)
    print(C)
    decrypt(n,C,d)

main()
