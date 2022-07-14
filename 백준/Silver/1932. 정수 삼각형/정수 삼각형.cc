#include <iostream>
#include <algorithm>

using namespace std;

int n;
int arr[505][505];
int d[505][505];

int main() {
	ios::sync_with_stdio(0);
	cin.tie(NULL);
	cout.tie(NULL);

	cin >> n;
	for (int i = 0;i < n;i++) {
		for (int j = 0;j <= i;j++) {
			cin >> arr[i][j];
		}
	}

	d[0][0] = arr[0][0];
	for (int i = 1;i < n;i++) {
		for (int j = 0;j <= i;j++) {
			if (j == 0) d[i][j] = d[i - 1][0] + arr[i][0];
			else if (j == i) d[i][j] = d[i - 1][j - 1] + arr[i][j];
			else d[i][j] = max(d[i - 1][j - 1], d[i - 1][j])+arr[i][j];
		}
	}
	int max_value = 0;
	for (int i = 0;i < n;i++) {
		if (d[n - 1][i] > max_value) {
			max_value = d[n - 1][i];
		}
	}
	cout << max_value;
}