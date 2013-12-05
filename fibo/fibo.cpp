#include <iostream>
#include <vector>

using std::cout;
using std::endl;
using std::vector;

static vector<int> *memo = new vector<int>();

int fibo(int n) {
  if (n < 0) {
    return -1;
  }
  int size = memo->size();
  if (n < size) {
    return memo->at(n);
  }
  for (int i = size; i <= n; i++) {
    memo->push_back(memo->at(i - 1) + memo->at(i - 2));
  }
  return memo->at(n);
}

int main() {
  memo->push_back(0);
  memo->push_back(1);
  cout << fibo(0) << endl;
  cout << fibo(1) << endl;
  cout << fibo(10000000) << endl;
  cout << fibo(10000000-1) << endl;
}
