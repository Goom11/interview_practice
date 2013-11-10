#include <iostream>
#include <stack>

using std::cout;
using std::endl;
using std::stack;

class StackWithMin {
  public:
    StackWithMin();
    void push(int item);
    int pop();
    int getMin();
    int size();
    bool empty();
    int top();
  private:
    stack<int> minStack;
    stack<int> actualStack;
};

StackWithMin::StackWithMin() {}

void StackWithMin::push(int item) {
  actualStack.push(item);
  if (minStack.empty() || item <= minStack.top()) {
    minStack.push(item);
  }
}

int StackWithMin::pop() {
  int item = actualStack.top();
  actualStack.pop();
  if (item == minStack.top()) {
    minStack.pop();
  }
  return item;
}

int StackWithMin::getMin() {
  return minStack.top();
}

int StackWithMin::size() {
  return actualStack.size();
}

bool StackWithMin::empty() {
  return (actualStack.size() == 0);
}

int StackWithMin::top() {
  return actualStack.top();
}

int main() {
  StackWithMin first;
  for (int i = 0; i < 5; i++) {
    first.push(i);
  }
  if (!first.empty()) {
    cout << "Not empty" << endl;
  }
  first.pop();
  cout << "Top is " << first.top() << endl;
  cout << "Stack contains " << first.size() << " items" << endl;
  cout << "The smallest element is " << first.getMin() << endl;
}
