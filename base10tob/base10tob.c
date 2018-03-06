#include <stdio.h>

// Converts base 10 integer to base b 
// b must be 1-9
void convertb10tobb(int n, int b) {
  if(n == 0)
    return;

  int num = n % b; 
  printf("%d", num);

  convertb10tobb(n / b, b);
}

int main(void) {
  convertb10tobb(255,2);
}
