#include <iostream>
#include <list>
#include <map>

using std::cout;
using std::endl;
using std::list;
using std::map;

void deleteDups(list<int>& n) {
  map<int, bool> table;
  list<int>::iterator n_it = n.begin();
  while (n_it != n.end()) {
    if (table[*n_it]) {
      n.erase(n_it);
      n_it--;
    } else {
      table[*n_it] = true;
    }
    n_it++;
  }
}

int main() {
  int nums[] = {1, 2, 3, 4, 4, 4, 5, 4, 2, 6, 1, 7, 865};
  list<int> num_list (nums, nums + 12);
  deleteDups(num_list);
  list<int>::iterator n_it = num_list.begin();
  while (n_it != num_list.end()) {
    cout << *n_it << endl;
    n_it++;
  }
}
