#include <iostream>
#include <algorithm>
using namespace std;

int n;
long long d[100];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;

	d[0] = 0;
	d[1] = 1;

	for (int i = 2;i <= n;i++) {
		d[i] = d[i - 1] + d[i - 2];
	}
	cout << d[n];
	return 0;
}