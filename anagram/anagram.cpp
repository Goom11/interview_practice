#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

bool anagram(string str1, string str2) {
  if (str1.length() != str2.length()) {
    false;
  }
  int char_set[256] = {0};
  for (int i = 0; i < str1.length(); i++) {
    char_set[str1[i]]++;
  }
  for (int i = 0; i < str2.length(); i++) {
    char_set[str2[i]]--;
  }
  for (int i = 0; i < 256; i++) {
    if (char_set[i] != 0) {
      return false;
    }
  }
  return true;
}


int main() {
  string a = "Hello";
  string b = "olelH";
  cout << a << " is ";
  if (!anagram(a, b)) {
    cout << "not";
  }
  cout << " an anagram of " << b << endl;
}
