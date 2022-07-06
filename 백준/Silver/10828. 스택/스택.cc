#include <iostream>
#include <stack>
#include<string>

using namespace std;
stack <int> s;
int n;

int main() {
	ios::sync_with_stdio(0);
	string instr;

	cin >> n;

	for (int i = 0;i < n;i++) {
		cin >> instr;
		int num;
		if (instr == "push") {
			cin >> num;
			s.push(num);
		}
		if (instr == "pop") {
			if (s.empty()) {
				cout << -1<<"\n";
			}
			else {
				num = s.top();
				cout << num << "\n";
				s.pop();
			}
		}
		if (instr == "size")
			cout << s.size() << "\n";;
		if (instr == "empty") {
			if (s.empty())
				cout << 1 << "\n";
			else
				cout << 0 << "\n";
		};
		if (instr == "top") {
			if (s.empty())
				cout << -1 << "\n";
			else
				cout << s.top() << "\n";
		}
	}
	return 0;
}