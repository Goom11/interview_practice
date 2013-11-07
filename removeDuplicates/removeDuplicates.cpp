#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

string removeDuplicates(string str) {
  int tail = 0;
  bool char_set[256] = {0};
  for (int i = 0; i < str.length(); i++) {
    if (!char_set[str[i]]) {
      str[tail] = str[i];
      tail++;
      char_set[str[i]] = true;
    }
  }
  str[tail] = 0;
  return str;
}


int main() {
  string a = "Hello";
  cout << a << " with duplicates removed is ";
  string b = removeDuplicates(a);
  cout << b << endl;
}
