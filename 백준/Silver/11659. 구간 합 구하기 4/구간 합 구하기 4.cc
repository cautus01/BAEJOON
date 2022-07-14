#include <iostream>

using namespace std;

int n,m;
int arr[100005];
int d[100005];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n >> m;
	for (int i = 1;i <= n;i++) {
		cin >> arr[i];
	}
	for (int i = 1;i <= n;i++) {
		d[i] = d[i - 1] + arr[i];
	}

	int a, b;
	for (int i = 0;i < m;i++) {
		cin >> a >> b;
		cout << d[b] - d[a-1] << "\n";
	}
}