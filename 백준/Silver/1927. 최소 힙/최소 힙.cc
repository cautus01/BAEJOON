#include <iostream>
#include <queue>

using namespace std;
int n;
unsigned int num;

int main() {
	ios::sync_with_stdio(0);

	cin.tie(NULL);
	cout.tie(NULL);
	cin >> n;
	priority_queue<int,vector<int>, greater<int>> pq;
	for (int i = 0;i < n;i++) {
		cin >> num;
		if (num == 0) {
			if (pq.empty()) {
				cout << 0 << "\n";
				continue;
			}
			cout<< pq.top()<< "\n";
			pq.pop();
		}
		else {
			pq.push(num);
		}
	}
}