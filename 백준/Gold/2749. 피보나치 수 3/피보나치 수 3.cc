#include <iostream>
using namespace std;

long long n;
int d[1500002];

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);

	cin >> n;
	d[0] = 0;
	d[1] = 1;
	for (int i = 2;i < 1500000;i++) {
		d[i] = (d[i - 1] + d[i - 2]) % 1000000;
	}
	cout << d[n % 1500000];
}