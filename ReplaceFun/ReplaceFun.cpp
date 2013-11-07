#include <iostream>

using std::cout;
using std::endl;

void ReplaceFun(char str1[], int length) {
  int newlen = length;
  for (int i = 0; i < length; i++) {
    if (str1[i] == ' ') {
      newlen += 3;
    }
  }
  char* new_str = new char[newlen];
  new_str[newlen] = 0;
  int front = 0;
  for (int i = 0; i < length; i++) {
    if (str1[i] == ' ') {
      new_str[front] = '%';
      new_str[front + 1] = '2';
      new_str[front + 2] = '0';
      front += 3;
    } else {
      new_str[front] = str1[i];
      front++;
    }
  }
  cout << new_str << endl;
}

int main() {
  char a[] = "a b c";
  int length = 6;
  cout << a << " with spaces replaced is ";
  ReplaceFun(a, length);
}
