#include <iostream>
#include <queue>
#include <string>

using namespace std;
int n;

int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	string instr;
	queue<int> Q;
	cin >> n;

	for (int i = 0;i < n;i++) {
		cin >> instr;
		int num;
		if (instr == "push") {
			cin >> num;
			Q.push(num);
		}
		if (instr == "pop") {
			if (Q.empty()) {
				cout << -1 << "\n";
			}
			else {
				num = Q.front();
				cout << num << "\n";
				Q.pop();
			}
		}
		if (instr == "size")
			cout << Q.size() << "\n";;
		if (instr == "empty") {
			if (Q.empty())
				cout << 1 << "\n";
			else
				cout << 0 << "\n";
		};
		if (instr == "front") {
			if (Q.empty())
				cout << -1 << "\n";
			else
				cout << Q.front() << "\n";
		}
		if (instr == "back") {
			if (Q.empty())
				cout << -1 << "\n";
			else
				cout << Q.back() << "\n";
		}
	}
	return 0;
}