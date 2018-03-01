import math

def euc_algorithm(a, b):
    # initialize matrix 
    matrix = [ [1, 0 , a], [0, 1, b]]

    # if one of the two equals zero then return the matrix 
    while True:
        
        # determine row to be subtracted from
        a1, b1 = matrix[0][2], matrix[1][2]

        if a1 == 0 or b1 == 0:
            break
    
        div = 1 
        sub_row = 1 
        row = 0

        if a1 > b1: # R1 - div*R2
            div = a1 // b1 # integer division 
        else: # R2 - div*R1
            div = b1 // a1
            sub_row = 0
            row = 1

        # perform componentwise multiplication on the row 
        sub_vector = [div*comp for comp in matrix[sub_row]]
        matrix[row] = [r_i - s_i for r_i,s_i in zip(matrix[row], sub_vector)]
        
    return matrix

def gcd(a,b):

    m = euc_algorithm(a,b)

    divisor = 1

    if m[0][2] == 0:
        divisor = m[1][2]
    else:
        divisor = m[0][2]

    s = str(m[0][0]) + " + " + str(m[1][0]) + "k"
    t = str(m[0][1]) + " + " + str(m[1][1]) + "k"

    print("GCD({}, {}) = {}".format(a,b, divisor))
    print("s = " + s)
    print("t = " + t)
    print("k = some integer\n")

def main():
    # Example calls 
    gcd(93,54)
    gcd(28,15)
    gcd(18, 17)
    gcd(20, 55)


main()
