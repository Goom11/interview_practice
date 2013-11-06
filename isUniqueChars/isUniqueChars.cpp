#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

bool isUniqueChars(string str) {
  bool char_set[256] = {0};
  for (int i = 0; i < str.length(); i++) {
    int val = str[i];
    if (char_set[val]) {
      return false;
    }
    char_set[val] = true;
  }
  return true;
}


int main() {
  string str1 = "SO NDUPE";
  cout << str1 << endl;
  if (isUniqueChars(str1)) {
    cout << "doesn't have duplicates" << endl;
  } else {
    cout << "has duplicates" << endl;
  }
  string str2 = "SO NDUPES";
  cout << str2 << endl;
  if (isUniqueChars(str2)) {
    cout << "doesn't have duplicates" << endl;
  } else {
    cout << "has duplicates" << endl;
  }
}
