#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;
using std::size_t;

bool isRotation(string str1, string str2) {
  int len = str1.length();
  if (len == str2.length() && len > 0) {
    string str1str1 = str1 + str1;
    size_t found = str1str1.find(str2);
    if (found == -1) {
      return false;
    } else {
      return true;
    }
  }
  return false;
}

int main() {
  string s1 = "apple";
  string s2 = "pleap";
  cout << s1 << " and " << s2 << " are";
  if (!isRotation(s1, s2)) {
    cout << " not";
  }
  cout << " rotated" << endl;
}
