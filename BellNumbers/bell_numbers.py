def factorial(n):
    sum = 0

    if(n == 1 or n == 0):
        return 1

    sum = factorial(n-1) * n;
    return sum


#   (n
#    k)  = (n!)/(k!(n-k)!)
def binomial_coefficient(n, k):
    return (factorial(n) / (factorial(k) * factorial(n-k)))


#   Bn = {  1 if n n == 0
#           Sum of (n-1 * Bk if n > 0
#	            k)
#	   From the definition in class 
def bell(n):
    if n < 0: return 0
    if n == 0: return 1

    full_sum = 0
    k = 0

    if (n > 0):
        full_sum = sum([binomial_coefficient(n-1, k) * bell(k) for k in range(0, n)])
    return full_sum


def main():
    for i in range(0, 21):
        print("bell(" + str(i) + "): " + str(bell(i)))

main()

        
