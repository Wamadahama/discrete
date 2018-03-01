#include <stdio.h>
#include <math.h>

#define M_E 2.71828182845904523536
#define int unsigned long long int

int factorial(int n) {
  int sum = 0;

  if (n == 1 || n == 0) 
    return 1;

  sum = factorial(n -1) * n;
  return sum; 
}

/*
   (n
    k)  = (n!)/(k!(n-k)!)
 */

int binomial_coefficient(int n, int k) {
  return (factorial(n) / (factorial(k) * factorial(n - k)));
}

/* 
   Bn = {  1 if n n == 0
           Sum of (n-1 * Bk if n > 0
	            k)
	   From the definition in class 
 */
int bell(int n) {
  

  if (n < 0)  return 0; // Error check 
  if (n == 0) return 1; // First conditon in the piecewise 


  // Second condition in the peicewise 
  int sum = 0, coeff = 0, k =0;

  if(n > 0) {
    for(k = 0; k <= n-1; ++k) {
	coeff = binomial_coefficient(n-1, k);
	sum += coeff * bell(k);
    }
  }

  return sum; 
}


int main(void) {
  puts("The first 15 bell numbers \n---------------------"); 

  for(int n = 0; n <= 15; ++n)
    printf("bell(%d) : %d\n", n, bell(n)); //  This method can only get the first 15 bell numbers 
  return 0; 
}

