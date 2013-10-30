#include <iostream>
#include <string>

using std::cout;
using std::endl;
using std::string;

int main() {
  for (int i = 1; i < 101; i++) {
    string s = "";
    if (i % 3 == 0) {
      s += "Fizz";
    }
    if (i % 5 == 0) {
      s += "Buzz";
    }
    if (s.length() == 0) {
      cout << i << endl;
    } else {
      cout << s << endl;
    }
  }
}
