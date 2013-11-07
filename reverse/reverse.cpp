#include <iostream>

using std::cout;
using std::endl;

void swap(char* a, char* b) {
  char tmp = *a;
  *a = *b;
  *b = tmp;
}

void reverse(char* str) {
  char* end = str;
  if (str) {
    while (*end) {
      end++;
    }
    end--;
    while (str < end) {
      swap(str, end);
      str++;
      end--;
    }
  }
}


int main() {
  char a[] = "Hello";
  cout << a << " reversed is ";
  reverse(a);
  cout << a << endl;
}
